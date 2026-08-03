#!/usr/bin/env python3
"""
===============================================================================
FINDING K CLOSEST ELEMENTS: WINDOW-START BINARY SEARCH APPROACH
===============================================================================

THE PROBLEM:
-------------------------------------------------------------------------------
Given a sorted array `arr` and a target value `x`, find the `k` closest elements 
to `x` in `arr`. The result should be returned in sorted order.

THE KEY QUESTION:
-------------------------------------------------------------------------------
"Why can we safely skip an entire half of the search space (low = mid + 1 vs high = mid)?"

THE MATHEMATICAL EXPLANATION (MONOTONICITY):
-------------------------------------------------------------------------------
1. Overlapping Window Comparison:
   A continuous window of size `k` starting at index `i` has elements from 
   arr[i] to arr[i + k - 1].
   
   If we slide the window one position right (to start at `i + 1`), the NEW window
   drops `arr[i]` and adds `arr[i + k]`. All elements in between remain identical.
   
   Therefore, deciding whether to move the window right comes down strictly to 
   comparing the distance of `arr[i]` to `x` vs `arr[i + k]` to `x`.

2. The Difference Function D(i):
   Let D(i) = (arr[i + k] - x) - (x - arr[i])
            = arr[i] + arr[i + k] - 2x

3. Monotonic Property:
   Since `arr` is sorted in non-decreasing order, as `i` increases:
     - `arr[i]` increases (or stays equal).
     - `arr[i + k]` increases (or stays equal).
     - `2x` is constant.
   
   Thus, D(i) is MONOTONICALLY INCREASING across the indices (it never goes down).

4. Why We Skip Halves in Binary Search:
   
   - CASE 1: If x - arr[mid] > arr[mid + k] - x  ==>  D(mid) < 0
     * `arr[mid + k]` is strictly closer to `x` than `arr[mid]`.
     * Because D(i) is monotonically increasing, for all indices i <= mid, 
       D(i) <= D(mid) < 0.
     * What this means: EVERY window starting at index 0, 1, ..., mid is 
       suboptimal compared to sliding right.
     * SAFELY ELIMINATE THE LEFT HALF: set `low = mid + 1`.

   - CASE 2: If x - arr[mid] <= arr[mid + k] - x  ==>  D(mid) >= 0
     * `arr[mid]` is closer (or equal) to `x` compared to `arr[mid + k]`.
     * Because D(i) is monotonically increasing, for all indices j > mid, 
       D(j) >= D(mid) >= 0.
     * What this means: EVERY window starting to the right of `mid` will only 
       include elements even further away from `x`.
     * SAFELY ELIMINATE THE RIGHT HALF: set `high = mid`.
===============================================================================
"""

def find_k_closest_elements(arr: list[int], k: int, x: int, verbose: bool = False) -> list[int]:
    """
    Finds the k closest elements to x in a sorted array arr using Binary Search.
    
    Time Complexity: O(log(N - k) + k)
    Space Complexity: O(1) auxiliary space (excluding result slice)
    """
    n = len(arr)
    low = 0
    high = n - k  # The window start index can at most be n - k
    
    if verbose:
        print(f"\n--- Running Binary Search for X={x}, K={k} ---")
        print(f"Array: {arr}")
        print(f"Initial Search Bounds for Window Start: low={low}, high={high}")
    
    step = 1
    while low < high:
        mid = (low + high) // 2
        
        # Distance from x to leftmost element of left window option
        left_dist = x - arr[mid]
        # Distance from x to rightmost element of right window option
        right_dist = arr[mid + k] - x
        
        if verbose:
            print(f"\nStep {step}: low={low}, high={high}, mid={mid}")
            print(f"  Comparing arr[mid]={arr[mid]} and arr[mid+k]={arr[mid + k]}")
            print(f"  Distance to arr[mid]: {abs(left_dist)}")
            print(f"  Distance to arr[mid+k]: {abs(right_dist)}")
        
        # If arr[mid + k] is closer to x than arr[mid],
        # shift search space strictly to the right.
        if left_dist > right_dist:
            if verbose:
                print(f"  -> arr[mid+k] is closer! Eliminating left range [0..{mid}]. New low = {mid + 1}")
            low = mid + 1
        else:
            if verbose:
                print(f"  -> arr[mid] is closer or equal! Eliminating right range [{mid + 1}..{high}]. New high = {mid}")
            high = mid
            
        step += 1
        
    if verbose:
        print(f"\nOptimal Window Start Index Found: low = {low}")
        print(f"Selected Window: arr[{low}:{low + k}] -> {arr[low : low + k]}")
        
    return arr[low : low + k]


# =============================================================================
# TEST SUITE
# =============================================================================

def run_tests():
    test_cases = [
        {
            "name": "Test 1: Target in middle, balanced split across left and right",
            "arr": [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56],
            "k": 4,
            "x": 35,
            "expected": [30, 35, 39, 42]
        },
        {
            "name": "Test 2: Target smaller than all array elements (all on right)",
            "arr": [10, 20, 30, 40, 50],
            "k": 3,
            "x": 5,
            "expected": [10, 20, 30]
        },
        {
            "name": "Test 3: Target larger than all array elements (all on left)",
            "arr": [10, 20, 30, 40, 50],
            "k": 3,
            "x": 100,
            "expected": [30, 40, 50]
        },
        {
            "name": "Test 4: Tie distance handling (prefer smaller values)",
            "arr": [1, 2, 3, 4, 5],
            "k": 4,
            "x": 3,
            "expected": [1, 2, 3, 4]
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print("=" * 80)
        print(f"RUNNING: {test['name']}")
        print(f'arr:{test["arr"]}, k:{test["k"]}, x:{test["x"]}')
        result = find_k_closest_elements(test["arr"], test["k"], test["x"], verbose=False)
        
        assert result == test["expected"], f"FAILED: Expected {test['expected']}, got {result}"
        print(f"SUCCESS: Returned {result}")

if __name__ == "__main__":
    run_tests()