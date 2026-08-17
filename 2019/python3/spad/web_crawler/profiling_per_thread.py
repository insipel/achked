"""
Attempt 2: correct multithreaded profiling -- one cProfile.Profile() per
worker thread, merged afterward.

The fix for Attempt 1's blind spot: instead of enabling a single profiler
on the main thread and hoping it covers everything, create a fresh
Profile() *inside* the function that actually runs on the worker thread,
and call .enable()/.disable() from within that same function. Since
Profile.enable() installs sys.setprofile() on whichever thread calls it,
and that call now happens on the worker thread itself, the hook is
installed exactly where the real work happens.

Each submitted task gets its own Profile object recording everything that
happened during that one call (ncalls/tottime/cumtime, driven by real
call/return events -- see attempt1's docstring for the mechanism). Because
cProfile.Profile is not designed to be shared safely across concurrently
enabled threads, we deliberately give each task its own instance rather
than one shared Profile -- and merge all of them afterward via
pstats.Stats(*profilers), which sums matching function records across
however many Profile objects you hand it. pstats.Stats() never touches
sys.setprofile itself; it's a pure reporting layer over data that's
already been collected.

Run directly: python3 attempt2_per_thread_cprofile.py
"""

import cProfile
import pstats
import threading
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


_thread_profilers = []
_profilers_lock = threading.Lock()  # guards the shared list, not the Profile objects themselves


def profiled_do_work():
    """Runs on a worker thread. Creates its own Profile, enables it on this
    thread specifically, runs the real work, then disables and stashes the
    result for merging back in the coordinating thread."""
    prof = cProfile.Profile()
    prof.enable()
    try:
        do_work()
    finally:
        prof.disable()
        with _profilers_lock:
            _thread_profilers.append(prof)


def run_in_pool_profiled(max_workers=4, num_tasks=8):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(profiled_do_work) for _ in range(num_tasks)]
        for f in futures:
            f.result()


if __name__ == "__main__":
    run_in_pool_profiled()

    print("=== per-thread cProfile, merged via pstats.Stats(*profilers) ===")
    merged = pstats.Stats(*_thread_profilers)
    merged.sort_stats("cumulative")
    merged.print_stats(10)

    print(
        "\nNotice: cpu_heavy_task and time.sleep now show real accumulated\n"
        "ncalls/cumtime -- because the profiling hook was installed on the\n"
        "worker threads themselves, exactly where those calls happened."
    )