#!/usr/bin/env python3
"""
===============================================================================
FINDING K CLOSEST ELEMENTS: BINARY SEARCH + TWO POINTERS APPROACH
===============================================================================

THE STRATEGY:
-------------------------------------------------------------------------------
1. Find Crossover Point (Binary Search):
   Use binary search (`bisect_left` or standard binary search) to locate the 
   insertion position of `x` in the sorted array `arr`.
   - `right` pointer starts at the insertion point (smallest element >= x).
   - `left` pointer starts immediately to its left (`right - 1`).

2. Expand Outward (Two Pointers):
   Compare elements at `left` and `right`:
   - Whichever element has a smaller absolute difference to `x` is selected, 
     and its pointer is moved outward.
   - If there is a tie in distance (|arr[left] - x| == |arr[right] - x|), 
     we prefer the smaller element (i.e., `left` pointer).
   - We repeat this until `k` elements are gathered.

3. Format Output:
   Return the collected `k` elements in sorted order.

COMPLEXITY:
-------------------------------------------------------------------------------
- Time Complexity: O(log N + k) 
  * O(log N) to find crossover point via binary search.
  * O(k) to collect the k elements with two pointers.
- Space Complexity: O(1) auxiliary space (excluding the output array).
===============================================================================
"""

import bisect


def find_k_closest_two_pointers(arr: list[int], k: int, x: int, verbose: bool = False) -> list[int]:
    """
    Finds the k closest elements to x in sorted array arr using Binary Search + Two Pointers.
    """
    n = len(arr)
    
    # Step 1: Find crossover/insertion point using binary search
    right = bisect.bisect_left(arr, x)
    left = right - 1
    
    if verbose:
        print(f"\n--- Running Two Pointers for X={x}, K={k} ---")
        print(f"Array: {arr}")
        print(f"Binary search crossover point: left_idx={left}, right_idx={right}")
    
    result = []
    
    # Step 2: Expand outwards until we collect k elements
    for step in range(1, k + 1):
        # Case A: Out of bounds on the left side -> must pick right
        if left < 0:
            picked = arr[right]
            if verbose:
                print(f"Step {step}: Left boundary reached. Picked right element: {picked}")
            result.append(picked)
            right += 1
            
        # Case B: Out of bounds on the right side -> must pick left
        elif right >= n:
            picked = arr[left]
            if verbose:
                print(f"Step {step}: Right boundary reached. Picked left element: {picked}")
            result.append(picked)
            left -= 1
            
        # Case C: Compare distances (|arr[left] - x| vs |arr[right] - x|)
        else:
            left_diff = abs(arr[left] - x)
            right_diff = abs(arr[right] - x)
            
            # Prefer smaller/equal distance on left (ties prefer smaller element)
            if left_diff <= right_diff:
                picked = arr[left]
                if verbose:
                    print(f"Step {step}: |{arr[left]} - {x}| ({left_diff}) <= |{arr[right]} - {x}| ({right_diff}). Picked left: {picked}")
                result.append(picked)
                left -= 1
            else:
                picked = arr[right]
                if verbose:
                    print(f"Step {step}: |{arr[left]} - {x}| ({left_diff}) > |{arr[right]} - {x}| ({right_diff}). Picked right: {picked}")
                result.append(picked)
                right += 1

    # Return result in sorted order
    return sorted(result)


# =============================================================================
# TEST SUITE
# =============================================================================

def run_tests():
    test_cases = [
        {
            "name": "Test 1: Balanced split across both sides",
            "arr": [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56],
            "k": 4,
            "x": 35,
            "expected": [30, 35, 39, 42]
        },
        {
            "name": "Test 2: Target smaller than all elements (all picked from right)",
            "arr": [10, 20, 30, 40, 50],
            "k": 3,
            "x": 5,
            "expected": [10, 20, 30]
        },
        {
            "name": "Test 3: Target larger than all elements (all picked from left)",
            "arr": [10, 20, 30, 40, 50],
            "k": 3,
            "x": 100,
            "expected": [30, 40, 50]
        },
        {
            "name": "Test 4: Distance tie handling (prefers smaller element)",
            "arr": [1, 2, 3, 4, 5],
            "k": 4,
            "x": 3,
            "expected": [1, 2, 3, 4]
        }
    ]
    
    for test in test_cases:
        print("=" * 80)
        print(f"RUNNING: {test['name']}")
        print(f'arr:{test["arr"]}, k:{test["k"]}, x:{test["x"]}')
        res = find_k_closest_two_pointers(test["arr"], test["k"], test["x"], verbose=False)
        assert res == test["expected"], f"FAILED: Expected {test['expected']}, got {res}"
        print(f"SUCCESS: Returned {res}")

if __name__ == "__main__":
    run_tests()