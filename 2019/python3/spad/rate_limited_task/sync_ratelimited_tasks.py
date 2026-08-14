#!/usr/bin/python3

import threading
import time

from concurrent.futures import ThreadPoolExecutor
from typing import List, TypeVar, Generic, Optional

T = TypeVar('T')

class ManualQueue(Generic[T]):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer : List[T] = []
        self.lock = threading.Lock()

        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)
    
    def put(self, item: T, timeout:Optional[float]=None) -> bool:
        with self.not_full:
            start_time = time.time()
            while len(self.buffer) >= self.capacity:
                if timeout is not None:
                    elapsed_time = time.time() - start_time
                    if elapsed_time >= timeout:
                        return False
                    self.not_full.wait(timeout=timeout-elapsed_time)
                else:
                    self.not_full.wait()

            self.buffer.append(item)
            self.not_empty.notify()
            print(f"enqueued task[{item}]")
            return True
    
    def get(self, timeout: Optional[float]=None) -> Optional[T]:
        with self.not_empty:
            start_time = time.time()
            while len(self.buffer) == 0:
                if timeout is not None:
                    elapsed_time = time.time() - start_time
                    if elapsed_time >= timeout:
                        return None
                    self.not_empty.wait(timeout=timeout-elapsed_time)
                else:
                    self.not_empty.wait()

            t = self.buffer.pop(0)
            print(f"processing task[{t}]")
            self.not_full.notify()
            return t

class ThreadedRateLimiter:
    def __init__(self, max_reqs:int, period:float):
        self.max_reqs = max_reqs
        self.period = period
        self.timestamps:List[float] = []
        self.rlock = threading.RLock()
    
    def admit(self):
        with self.rlock:
           while True:
                now = time.time()

                self.timestamps = [t for t in self.timestamps if now - t < self.period]
                if len(self.timestamps) < self.max_reqs:
                    self.timestamps.append(now)
                    return
                
                sleep_time = self.period - (now - self.timestamps[0])
                if sleep_time:
                    time.sleep(sleep_time)

class ConcurrentTask:
    def __init__(self, max_workers=4,
                 queue_capacity=10, timeout:Optional[float]=None):
        self.max_workers = max_workers
        self.queue = ManualQueue[int](queue_capacity)
        self.shutdown_event = threading.Event()
        self.timeout = timeout
        self.rateLimiter = ThreadedRateLimiter(max_reqs=2, period=1)

        print(f"concurrent task inited")
    
    def worker(self, worker_id: int):
        print(f"called ccrnt worker")
        while not self.shutdown_event.is_set():
            t = self.queue.get(self.timeout)
            if t is None:
                continue

            self.rateLimiter.admit()
            print(f"worker[{worker_id}] processed task[{t}]")
    
    def run(self, num_tasks:int):
        print(f"about to process total {num_tasks}")
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self.worker, i) for i in range(1,self.max_workers+1)]

            for task in range(1,num_tasks+1):
                while not self.queue.put(item=task,timeout=self.timeout):
                    pass
                print(f"put task[{task}] for processing")
            
            while True:
                if not len(self.queue.buffer):
                    break
                time.sleep(0.1)
            
            self.shutdown_event.set()

            for f in futures:
                f.result()

        print(f" ---- Task processing done --- ")

if __name__ == "__main__":
    total_tasks = 15
    task = ConcurrentTask(max_workers=2, queue_capacity=5, timeout=0.1)
    task.run(total_tasks)