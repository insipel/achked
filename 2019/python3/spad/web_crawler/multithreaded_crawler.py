import threading
import time
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup


class ConcurrentWebCrawler:
    """Bounded, single-pass multithreaded crawler.

    Given a seed URL, crawls every reachable page on the same hostname and
    returns once the frontier is exhausted -- this is intentionally a bounded
    batch job (it terminates and returns a result), not an always-on daemon.

    Coordination model: worker threads only fetch+parse one URL and return
    the links they found. They never touch shared state and never submit
    further work themselves -- all bookkeeping (the visited set, deciding
    what to crawl next, deciding when to stop) happens in the single
    coordinating thread via a wait()-loop over an evolving set of futures.

    This sidesteps two bugs a naive Thread + Queue design is prone to:
      - workers retiring early on an idle timeout, silently losing
        parallelism if discovery is bursty/uneven (ThreadPoolExecutor's
        workers only block on its internal queue -- no self-retirement);
      - exceptions from a failed fetch getting swallowed and printed deep
        inside a worker instead of surfacing to whoever's driving the crawl
        (here they raise from future.result() in the coordinating loop).

    Because only the coordinating thread ever mutates `visited`, no lock is
    needed around it -- the concurrency is confined entirely to the fetch
    step, which is stateless with respect to the crawler's own bookkeeping.
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
        visited URLs once the frontier is exhausted."""
        if not self._is_allowed(self.seed_url):
            print(f"[Skipped] {self.seed_url} disallowed by robots.txt")
            return set()

        visited = {self.seed_url}

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self._fetch_and_parse, self.seed_url)}

            while futures:
                done, futures = wait(futures, return_when=FIRST_COMPLETED)
                for future in done:
                    try:
                        new_links = future.result()
                    except Exception as e:
                        print(f"[Error] fetch failed: {e}")
                        continue

                    for link in new_links:
                        if link in visited or len(visited) >= self.max_pages:
                            continue
                        visited.add(link)
                        futures.add(executor.submit(self._fetch_and_parse, link))

        print(f"[Complete] Crawled {len(visited)} pages.")
        return visited


# Example Usage:
if __name__ == "__main__":
    seed = "https://example.com"
    crawler = ConcurrentWebCrawler(seed_url=seed, max_workers=5, max_pages=500)
    result = crawler.start()
    print(f"Visited {len(result)} URLs")
