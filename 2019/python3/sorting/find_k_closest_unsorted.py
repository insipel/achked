import heapq

"""
PROBLEM STATEMENT:
Given an unsorted array of integers `arr`, a target value `x`, and an integer `k`,
find the `k` closest numbers to `x` in `arr`.

Distance Criterion:
- The distance between an element `num` and target `x` is measured as `abs(num - x)`.
- If two elements have the same absolute distance to `x`, the smaller number is 
  typically prioritized (or they are resolved based on proximity/value).

APPROACHES & ALGORITHMS:

1. Max-Heap (Priority Queue) Approach [Implemented Below]
   - We maintain a Max-Heap of size 'k' to store the 'k' closest elements seen so far.
   - Python's `heapq` module provides a Min-Heap by default, so we push tuple pairs 
     `(-distance, -value)` to simulate a Max-Heap.
   - For each element in the array:
     a. Calculate distance `dist = abs(num - x)`.
     b. Push `(-dist, -num)` onto the heap.
     c. If heap size exceeds `k`, pop the max element (the one furthest from `x`).
   - After processing all N elements, the heap contains the `k` closest numbers.

2. Quickselect Approach (Alternative O(N) average time)
   - Compute distances for all elements.
   - Use Quickselect (Partition algorithm) to find the k-th smallest distance.
   - All elements to the left of the k-th element in the partitioned array form 
     the k closest elements.
"""


def find_k_closest_max_heap(arr: list[int], k: int, x: int) -> list[int]:
    """Finds the k closest numbers to x using a Max-Heap of size k.

    Time Complexity: O(N log k)
    Space Complexity: O(k)
    """
    if not arr or k <= 0:
        return []

    if k >= len(arr):
        return arr

    # Max-Heap to store up to k elements
    # Tuple format: (-distance, -value) to make min-heap act as max-heap
    max_heap = []

    for num in arr:
        dist = abs(num - x)

        # Push negative distance and negative num into min-heap (simulating max-heap)
        heapq.heappush(max_heap, (-dist, -num))

        # If heap exceeds size k, remove the furthest element
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    # Extract original values from the heap
    result = [-num for (_, num) in max_heap]

    # Optional: Return in sorted order relative to distance/value for clarity
    result.sort(key=lambda item: (abs(item - x), item))
    return result


def find_k_closest_quickselect(arr: list[int], k: int, x: int) -> list[int]:
    """Finds the k closest numbers to x using Quickselect.

    Time Complexity: O(N) average, O(N^2) worst-case
    Space Complexity: O(N) for storing distance pairs
    """

    if not arr or k <= 0:
        return []
    if k >= len(arr):
        return arr

    # Array of tuples: (distance, value)
    pairs = [(abs(num - x), num) for num in arr]

    def quickselect(left: int, right: int, k_target: int):
        if left >= right:
            return

        # Simple partition scheme using rightmost element as pivot
        pivot_dist, _ = pairs[right]
        store_idx = left

        for i in range(left, right):
            if pairs[i][0] < pivot_dist or (
                pairs[i][0] == pivot_dist and pairs[i][1] <= pairs[right][1]
            ):
                pairs[i], pairs[store_idx] = pairs[store_idx], pairs[i]
                store_idx += 1

        pairs[store_idx], pairs[right] = pairs[right], pairs[store_idx]

        if store_idx == k_target:
            return
        elif store_idx < k_target:
            quickselect(store_idx + 1, right, k_target)
        else:
            quickselect(left, store_idx - 1, k_target)

    quickselect(0, len(pairs) - 1, k)
    result = [val for _, val in pairs[:k]]
    result.sort(key=lambda item: (abs(item - x), item))
    return result


# ==========================================
# TEST RUNNER & VERIFICATION
# ==========================================
if __name__ == "__main__":
    test_cases = [
        {
            "name": "Standard Unsorted Array",
            "arr": [10, 2, 14, 4, 7, 6],
            "k": 3,
            "x": 5,
        },
        {
            "name": "Target Outside Range (Smaller)",
            "arr": [20, 15, 30, 25, 40],
            "k": 2,
            "x": 5,
        },
        {
            "name": "Target Outside Range (Larger)",
            "arr": [1, 3, 7, 8, 2],
            "k": 3,
            "x": 10,
        },
        {
            "name": "Ties in Distances (Equal absolute differences)",
            "arr": [-10, 5, 15, 25, 35],
            "k": 2,
            "x": 10,
        },
        {"name": "k equals Array Size", "arr": [5, 1, 9, 3], "k": 4, "x": 5},
        {
            "name": "Array with Negative Numbers",
            "arr": [-2, -5, 3, 8, -1, 0],
            "k": 3,
            "x": -2,
        },
    ]

    print("=" * 70)
    print("      FIND K CLOSEST NUMBERS IN AN UNSORTED ARRAY - TEST RUNS      ")
    print("=" * 70)

    for i, test in enumerate(test_cases, 1):
        arr, k, x = test["arr"], test["k"], test["x"]

        # Run Max-Heap Approach
        heap_res = find_k_closest_max_heap(arr, k, x)

        # Run Quickselect Approach
        qs_res = find_k_closest_quickselect(arr, k, x)

        print(f"\nTest Case {i}: {test['name']}")
        print(f"  Input Array : {arr}")
        print(f"  Target (x)  : {x}")
        print(f"  k           : {k}")
        print(f"  Result (Heap Method)       : {heap_res}")
        print(f"  Result (Quickselect Method): {qs_res}")
        print("-" * 70)