"""
===============================================================================
PROBLEM STATEMENT: Sort a Nearly Sorted (or K-Sorted) Array
===============================================================================
Given an array `arr` of `N` elements, where each element is at most `K` positions 
away from its target sorted position, sort the array in ascending order.

Input:
  - arr: List[int] - A K-sorted array
  - k: int - Maximum distance any element is from its correct sorted index

Output:
  - List[int] - Fully sorted array in O(N log K) time
===============================================================================
ALGORITHM EXPLANATION: Min-Heap Sliding Window
===============================================================================
1. CORE INTUITION:
   In a K-sorted array, the correct element for index `i` is guaranteed to be 
   within the window of indices `[i, i + K]`. Therefore, the overall minimum 
   element of the entire array must lie within the first `K + 1` elements 
   (indices 0 through K).

2. DATA STRUCTURE: Min-Heap (Priority Queue)
   - We construct a min-heap containing the first `K + 1` elements.
   - The smallest element in the min-heap is guaranteed to belong at the next 
     available position in the sorted result.

3. SLIDING WINDOW PROCESS:
   - Extract (pop) the minimum element from the min-heap and place it in the array.
   - Push the next available element from the remaining unvisited array elements 
     into the min-heap.
   - Repeat until all elements from the input array have been pushed.
   - Once the array traversal is complete, pop all remaining elements from the 
     min-heap and place them in the output array.

4. COMPLEXITY:
   - Time Complexity: O(N log K)
     pushed and popped from a heap of max size (K + 1), taking O(log K) per element.
   - Auxiliary Space Complexity: O(K) for maintaining the min-heap of size K + 1.
===============================================================================
"""

import heapq


def sort_k_sorted_array(arr: list[int], k: int) -> list[int]:
    """
    Sorts a nearly sorted (K-sorted) array using a Min-Heap.
    Modifies and returns the array in sorted order.
    """
    n = len(arr)
    if n <= 1 or k == 0:
        return arr

    # Step 1: Create a Min-Heap with the first min(K + 1, N) elements
    # Using min(k + 1, n) handles cases where K is larger than or equal to array size
    heap_size = min(k + 1, n)
    min_heap = arr[:heap_size]
    heapq.heapify(min_heap)

    # Pointer to track where the next smallest element should be placed
    target_idx = 0

    # Step 2: Process the rest of the elements in the array
    for i in range(heap_size, n):
        # Extract the minimum element from the heap and place it at target_idx
        arr[target_idx] = heapq.heappop(min_heap)
        target_idx += 1

        # Insert the next element from the array into the heap
        heapq.heappush(min_heap, arr[i])

    # Step 3: Pop the remaining elements from the min-heap
    while min_heap:
        arr[target_idx] = heapq.heappop(min_heap)
        target_idx += 1

    return arr


# =============================================================================
# TEST EXAMPLES & DRIVER CODE
# =============================================================================
if __name__ == "__main__":
    test_cases = [
        {
            "description": "Standard K-sorted array (K=2)",
            "arr": [3, 2, 1, 5, 4, 7, 6, 9, 8],
            "k": 2,
        },
        {
            "description": "Array where K=3",
            "arr": [2, 6, 3, 12, 56, 8],
            "k": 3,
        },
        {
            "description": "Already sorted array (K=1)",
            "arr": [1, 2, 3, 4, 5],
            "k": 1,
        },
        {
            "description": "Reverse pairs (K=1)",
            "arr": [2, 1, 4, 3, 6, 5],
            "k": 1,
        },
        {
            "description": "K is equal to array length - 1 (K=4)",
            "arr": [10, 9, 8, 7, 47],
            "k": 4,
        },
    ]

    print("=" * 70)
    print(" SORT NEARLY SORTED (K-SORTED) ARRAY - TEST RESULTS ")
    print("=" * 70)

    for idx, test in enumerate(test_cases, 1):
        input_arr = list(test["arr"])  # Make a copy for display
        k = test["k"]
        expected = sorted(input_arr)
        result = sort_k_sorted_array(list(input_arr), k)

        print(f"\nTest #{idx}: {test['description']}")
        print(f"  Input Array  : {input_arr}")
        print(f"  Value of K   : {k}")
        print(f"  Sorted Output: {result}")
        print(f"  Expected     : {expected}")
        print(f"  Status       : {'✅ PASSED' if result == expected else '❌ FAILED'}")

    print("\n" + "=" * 70)
