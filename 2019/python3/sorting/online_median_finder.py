#!/usr/bin/env python3
"""
Online Median Calculation (Finding Median from a Data Stream)
=============================================================

Problem Description:
--------------------
Design a data structure that supports adding numbers from a data stream and
retrieving the current median of all numbers added so far in O(1) time.

Median Definition:
- If the size of the list is even, the median is the average of the two middle values.
- If the size of the list is odd, the median is the middle value.

Approach:
---------
Two Heaps Technique (Max-Heap for lower half + Min-Heap for upper half)
Python's `heapq` module implements Min-Heaps by default. To simulate a Max-Heap,
we store negated values (-val).
"""

import heapq


class MedianFinder:
    def __init__(self):
        """
        Initializes two heaps:
        - self.small_half: Max-Heap (stores smaller half, values negated)
        - self.large_half: Min-Heap (stores larger half)
        """
        self.small_half = []  # Max-heap (store negated numbers)
        self.large_half = []  # Min-heap (store standard numbers)

    def add_num(self, num: int) -> None:
        """
        Adds a number from the data stream into the data structure.
        Time Complexity: O(log N)
        """
        # Step 1: Push to max-heap (small_half)
        heapq.heappush(self.small_half, -num)

        # Step 2: Ensure order invariant: max(small_half) <= min(large_half)
        # Move largest element from small_half to large_half
        max_from_small = -heapq.heappop(self.small_half)
        heapq.heappush(self.large_half, max_from_small)

        # Step 3: Ensure size invariant: len(small_half) >= len(large_half)
        # small_half is allowed to have at most 1 extra element
        if len(self.large_half) > len(self.small_half):
            min_from_large = heapq.heappop(self.large_half)
            heapq.heappush(self.small_half, -min_from_large)

    def find_median(self) -> float:
        """
        Returns the current median of all elements added so far.
        Time Complexity: O(1)
        """
        if len(self.small_half) > len(self.large_half):
            # Odd number of elements: root of max-heap
            return float(-self.small_half[0])
        else:
            # Even number of elements: average of top elements of both heaps
            return (-self.small_half[0] + self.large_half[0]) / 2.0


def run_tests():
    """
    Executes sample test scenarios and prints stream updates and medians.
    """
    print("=" * 65)
    print("        ONLINE MEDIAN CALCULATION - TEST EXECUTIONS")
    print("=" * 65)

    test_cases = [
        {
            "name": "Test 1: Standard Stream",
            "stream": [6, 10, 2, 6, 5, 0, 6, 3, 1, 100]
        },
        {
            "name": "Test 2: Monotonically Increasing Stream",
            "stream": [1, 2, 3, 4, 5, 6, 7]
        },
        {
            "name": "Test 3: Stream with Duplicates and Negatives",
            "stream": [-5, 10, -5, 20, 0, 0]
        }
    ]

    for test in test_cases:
        print(f"\n--- {test['name']} ---")
        stream = test["stream"]
        print(f"Full Input Stream: {stream}\n")
        
        mf = MedianFinder()
        current_elements = []

        print(f"{'Step':<6} | {'Added Num':<10} | {'Current Stream':<30} | {'Median':<8}")
        print("-" * 65)

        for step, num in enumerate(stream, 1):
            current_elements.append(num)
            mf.add_num(num)
            med = mf.find_median()
            print(f"{step:<6} | {num:<10} | {str(current_elements):<30} | {med:<8.2f}")


if __name__ == "__main__":
    run_tests()