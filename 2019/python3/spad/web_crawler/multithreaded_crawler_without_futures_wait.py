import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup


class ConcurrentWebCrawler:
    """Same crawler as multithreaded_crawler.py, different completion-
    notification mechanism -- no concurrent.futures.wait() in the loop.

    The wait()-based version calls wait(futures, return_when=FIRST_COMPLETED)
    once per completion. Each call is O(n) in the size of the *currently
    pending* futures set: it acquires a lock on every pending future to
    register a waiter, then does it again to tear the waiter down once
    woken (see CPython's concurrent/futures/_base.py -- `wait()` does
    `with _AcquireFutures(fs)` on the way in and `for f in fs: f._waiters
    .remove(waiter)` on the way out). Looped once per completion, the
    *cumulative* cost across a crawl scales with total completions times
    average pending-set size -- worse than linear if the frontier stays
    wide for a while.

    This version replaces that with future.add_done_callback(): each
    future notifies a thread-safe queue.Queue the instant it finishes,
    an O(1) push regardless of how many other futures are still pending.
    The coordinator just drains that queue with queue.get() -- no
    rescanning of the pending set on every wakeup, ever.

    Trade-off worth knowing: add_done_callback()'s callback runs on
    whichever thread actually completes the future (normally a pool
    worker thread, occasionally the coordinator itself if the future was
    already done by the time the callback was attached -- concurrent.
    futures handles that race for you and invokes it immediately in that
    case). So the callback here must stay trivial and must not touch
    `visited` or any crawler-wide bookkeeping directly -- it only pushes
    the future onto the queue. All actual decision-making (has this URL
    been seen, should we submit more work, when do we stop) still happens
    only in the coordinator thread, exactly as in the wait()-based
    version. Only the notification mechanism changed, not who's allowed
    to touch shared state.
    """

    DEFAULT_HEADERS = {"User-Agent": "PracticeCrawler/1.0 (+https://example.invalid/bot)"}

    def __init__(self, seed_url: str, max_workers: int = 5, max_pages: int = 1000,
                 requests_per_second: float = 2.0, respect_robots: bool = True):
        self.seed_url = seed_url
        self.domain = urlparse(seed_url).netloc
        self.max_workers = max_workers
        self.max_pages = max_pages  # safety valve -- real sites can be effectively unbounded

        # Shared rate limiter: keeps us polite to the target host regardless
        # of how many worker threads are hitting it concurrently. Lock is
        # only held for the O(1) bookkeeping, never across time.sleep().
        self._rate_lock = threading.Lock()
        self._min_interval = 1.0 / requests_per_second if requests_per_second > 0 else 0.0
        self._next_allowed_time = 0.0

        self._robot_parser = self._load_robots(seed_url) if respect_robots else None

    # ---- politeness ----------------------------------------------------

    def _load_robots(self, seed_url: str):
        parsed = urlparse(seed_url)
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
        parser = RobotFileParser()
        try:
            response = requests.get(robots_url, timeout=5, headers=self.DEFAULT_HEADERS)
            parser.parse(response.text.splitlines() if response.status_code == 200 else [])
        except requests.RequestException:
            parser.parse([])  # unreachable robots.txt -> fail open (treat as allow-all)
        return parser

    def _is_allowed(self, url: str) -> bool:
        if self._robot_parser is None:
            return True
        return self._robot_parser.can_fetch(self.DEFAULT_HEADERS["User-Agent"], url)

    def _throttle(self):
        with self._rate_lock:
            now = time.monotonic()
            wait_time = max(0.0, self._next_allowed_time - now)
            self._next_allowed_time = max(now, self._next_allowed_time) + self._min_interval
        # Lock released before sleeping -- other threads can compute their
        # own wait time concurrently instead of queuing behind this one.
        if wait_time > 0:
            time.sleep(wait_time)

    # ---- url handling ----------------------------------------------------

    def _is_same_domain(self, url: str) -> bool:
        parsed = urlparse(url)
        return parsed.netloc == self.domain or parsed.netloc == ""

    def _normalize_url(self, base_url: str, link: str) -> str:
        """Resolves relative links and strips fragments so #section anchors
        don't get treated as distinct pages."""
        joined = urljoin(base_url, link)
        return urlparse(joined)._replace(fragment="").geturl()

    def _fetch_and_parse(self, url: str):
        """Runs in a worker thread. Touches no crawler-wide mutable state --
        safe to run concurrently with no locking beyond the rate limiter.
        Raises on request failure rather than swallowing it, so the
        coordinating loop can decide what to do about it."""
        self._throttle()
        print(f"[Crawling] {url}")
        response = requests.get(url, timeout=5, headers=self.DEFAULT_HEADERS)

        content_type = response.headers.get("Content-Type", "")
        if "text/html" not in content_type or response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        discovered = []
        for anchor in soup.find_all("a", href=True):
            absolute_url = self._normalize_url(url, anchor["href"])
            if self._is_same_domain(absolute_url) and self._is_allowed(absolute_url):
                discovered.append(absolute_url)
        return discovered

    # ---- orchestration ----------------------------------------------------

    def start(self) -> set:
        """Coordinates the crawl from a single thread and returns the set of
        visited URLs once the frontier is exhausted. Completion notices
        arrive via a queue fed by future.add_done_callback() instead of a
        wait()-loop -- see class docstring for why."""
        if not self._is_allowed(self.seed_url):
            print(f"[Skipped] {self.seed_url} disallowed by robots.txt")
            return set()

        visited = {self.seed_url}
        completed: "queue.Queue" = queue.Queue()  # O(1) push/pop, no rescanning of pending work
        pending_count = 0  # touched only by the coordinator thread -- see submit()/main loop

        def on_done(future):
            # Runs on whichever thread completes the future -- keep it
            # trivial and side-effect-free beyond this enqueue. All actual
            # decision-making happens below, in the coordinator.
            completed.put(future)

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:

            def submit(url):
                nonlocal pending_count
                future = executor.submit(self._fetch_and_parse, url)
                future.add_done_callback(on_done)
                pending_count += 1

            submit(self.seed_url)

            while pending_count > 0:
                future = completed.get()  # blocks until *something* finishes; O(1), no rescanning
                pending_count -= 1

                try:
                    new_links = future.result()
                except Exception as e:
                    print(f"[Error] fetch failed: {e}")
                    continue

                for link in new_links:
                    if link in visited or len(visited) >= self.max_pages:
                        continue
                    visited.add(link)
                    submit(link)

        print(f"[Complete] Crawled {len(visited)} pages.")
        return visited


# Example Usage:
if __name__ == "__main__":
    seed = "https://example.com"
    crawler = ConcurrentWebCrawler(seed_url=seed, max_workers=5, max_pages=500)
    result = crawler.start()
    print(f"Visited {len(result)} URLs")
