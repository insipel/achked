"""
Attempt 1: naive cProfile around a multithreaded workload.

`Profile.enable()` calls sys.setprofile(...) under the hood, which installs
a call/return hook on ONLY the thread that calls it (see
threading.setprofile()'s docstring -- it exists specifically to propagate a
profile function to *new* threads, which proves sys.setprofile() doesn't do
that on its own). Here we enable the profiler on the main thread, then hand
work off to a ThreadPoolExecutor -- the 4 worker threads it spawns start
with no profiling hook installed at all, so every call/return event inside
do_work/cpu_heavy_task/cpu_light_task happens on a thread cProfile was never
told to watch. Those events are not misattributed anywhere -- they're
simply never recorded.

What the main thread *is* doing while workers run is blocking inside
Future.result() -> ...-> some_lock.acquire(), waiting for a worker to
finish. That's a real call on the main thread, so cProfile times it
correctly -- which is exactly why the output below shows nearly all the
wall-clock time as "spent" in `_thread.lock.acquire`, even though the CPU
was actually busy the whole time on threads this profiler couldn't see.

Run directly: python3 attempt1_naive_cprofile.py
"""

import cProfile
import pstats
import time
from concurrent.futures import ThreadPoolExecutor


def cpu_light_task():
    time.sleep(0.01)


def cpu_heavy_task():
    total = 0
    for i in range(2_000_000):
        total += i * i
    return total


def do_work():
    for _ in range(3):
        cpu_light_task()
    cpu_heavy_task()


def run_in_pool(max_workers=4, num_tasks=8):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_work) for _ in range(num_tasks)]
        for f in futures:
            f.result()


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    run_in_pool()
    profiler.disable()

    print("=== naive cProfile (installed only on the main/calling thread) ===")
    stats = pstats.Stats(profiler)
    stats.sort_stats("cumulative")
    stats.print_stats(10)

    print(
        "\nNotice: do_work / cpu_heavy_task / cpu_light_task never appear above.\n"
        "The time shown is almost entirely '_thread.lock.acquire' -- the main\n"
        "thread blocked waiting on Future.result(), not the actual work, which\n"
        "ran invisibly on worker threads this profiler was never installed on."
    )