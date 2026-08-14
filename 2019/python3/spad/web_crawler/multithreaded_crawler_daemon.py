from queue import Queue
from threading import Lock, Thread
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests


class ConcurrentWebCrawler:

  def __init__(self, seed_url: str, max_threads: int = 4):
    self.seed_url = seed_url
    self.parsed_seed = urlparse(seed_url)
    self.domain = self.parsed_seed.netloc

    # Thread-safe data structures
    self.queue = Queue()
    self.visited = set()
    self.visited_lock = Lock()

    self.max_threads = max_threads

    # Seed the queue
    self.queue.put(seed_url)
    with self.visited_lock:
      self.visited.add(seed_url)

  def _is_same_domain(self, url: str) -> bool:
    """Ensures the crawler stays within the same domain."""
    parsed = urlparse(url)
    return parsed.netloc == self.domain or parsed.netloc == ""

  def _normalize_url(self, base_url: str, link: str) -> str:
    """Resolves relative links and strips fragments."""
    joined = urljoin(base_url, link)
    parsed = urlparse(joined)
    # Reconstruct URL without fragment (#section) to avoid duplicate visits
    clean_url = parsed._replace(fragment="").geturl()
    return clean_url

  def _worker(self):
    """Worker thread that continuously fetches and extracts links."""
    while True:
      try:
        # Get URL from queue with a timeout so threads can exit gracefully
        current_url = self.queue.get(timeout=3)
      except Exception:
        # Queue is empty and timed out
        break

      try:
        print(f"[Crawling] {current_url}")
        response = requests.get(
            current_url, timeout=5, headers={"User-Agent": "SecureCrawler/1.0"}
        )

        # Only parse HTML responses
        if "text/html" not in response.headers.get("Content-Type", ""):
          continue

        if response.status_code == 200:
          soup = BeautifulSoup(response.text, "html.parser")

          for anchor in soup.find_all("a", href=True):
            raw_link = anchor["href"]
            absolute_url = self._normalize_url(current_url, raw_link)

            if self._is_same_domain(absolute_url):
              with self.visited_lock:
                if absolute_url not in self.visited:
                  self.visited.add(absolute_url)
                  self.queue.put(absolute_url)

      except requests.RequestException as e:
        print(f"[Error] Failed to fetch {current_url}: {e}")
      finally:
        # Mark the task as done in the queue
        self.queue.task_done()

  def start(self):
    """Spawns worker threads and runs the crawl until the queue is empty."""
    threads = []

    for _ in range(self.max_threads):
      t = Thread(target=self._worker)
      t.daemon = True
      t.start()
      threads.append(t)

    # Wait until all items in the queue have been processed
    self.queue.join()
    print("[Complete] Crawling finished successfully.")


# Example Usage:
if __name__ == "__main__":
  seed = "https://example.com"
  crawler = ConcurrentWebCrawler(seed_url=seed, max_threads=5)
  crawler.start()