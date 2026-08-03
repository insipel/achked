#!/usr/bin/env python3

def detect_is_ascending(nums: list[int]) -> bool:
    """
    Detects whether the array was sorted in ascending or descending order
    before rotation in O(1) time by comparing non-pivot adjacent pairs.
    """
    n = len(nums)
    if n <= 1:
        return True

    increments = 0
    decrements = 0

    # Inspect up to the first 3 consecutive adjacent pairs
    for i in range(min(3, n - 1)):
        if nums[i] < nums[i + 1]:
            increments += 1
        elif nums[i] > nums[i + 1]:
            decrements += 1

    return increments >= decrements


def find_pivot(nums: list[int], is_ascending: bool) -> int:
    """
    Finds the pivot (reset point index) using binary search.
    Requires knowing the sorting direction first.
    """
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        if is_ascending:
            # For ascending order, the break occurs where mid > high
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        else:
            # For descending order, the break occurs where mid < high
            if nums[mid] < nums[high]:
                low = mid + 1
            else:
                high = mid

    return low


def binary_search(nums: list[int], low: int, high: int, target: int, is_ascending: bool) -> int:
    """Standard binary search on a sorted slice [low...high]."""
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid

        if is_ascending:
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[mid] > target:
                low = mid + 1
            else:
                high = mid - 1

    return -1


def search_rotated_array(nums: list[int], target: int) -> int:
    """
    Searches for target in a rotated sorted array (ascending or descending).
    Returns the index if found, else -1.
    """
    if not nums:
        return -1

    # Step 1: Detect direction in O(1) time
    is_ascending = detect_is_ascending(nums)

    # Step 2: Find pivot (reset point) using direction-aware binary search
    pivot = find_pivot(nums, is_ascending)

    # Step 3: Search in the left or right sorted subarray
    # Check left subarray: [0 ... pivot - 1]
    res = binary_search(nums, 0, pivot - 1, target, is_ascending)
    if res != -1:
        return res

    # Check right subarray: [pivot ... len(nums) - 1]
    return binary_search(nums, pivot, len(nums) - 1, target, is_ascending)


# ==========================================
# TEST EXAMPLES (Simple Inputs)
# ==========================================
if __name__ == "__main__":
    tests = [
        # Test 1: Simple Ascending Rotated Array
        {"nums": [4, 5, 1, 2, 3], "target": 1, "expected": 2, "desc": "Ascending rotated, search middle target"},
        {"nums": [4, 5, 1, 2, 3], "target": 5, "expected": 1, "desc": "Ascending rotated, search left half"},
        {"nums": [4, 5, 1, 2, 3], "target": 9, "expected": -1, "desc": "Ascending rotated, target missing"},

        # Test 2: Simple Descending Rotated Array
        {"nums": [2, 1, 5, 4, 3], "target": 5, "expected": 2, "desc": "Descending rotated, search pivot target"},
        {"nums": [2, 1, 5, 4, 3], "target": 1, "expected": 1, "desc": "Descending rotated, search left half"},
        {"nums": [2, 1, 5, 4, 3], "target": 8, "expected": -1, "desc": "Descending rotated, target missing"},

        # Test 3: Un-rotated Simple Arrays
        {"nums": [1, 2, 3, 4, 5], "target": 3, "expected": 2, "desc": "Un-rotated ascending"},
        {"nums": [5, 4, 3, 2, 1], "target": 2, "expected": 3, "desc": "Un-rotated descending"},
    ]

    print("--- RUNNING TESTS ---\n")
    for i, test in enumerate(tests, 1):
        arr = test["nums"]
        target = test["target"]
        expected = test["expected"]
        
        result = search_rotated_array(arr, target)
        status = "PASSED ✅" if result == expected else f"FAILED ❌"

        print(f"Test {i} ({test['desc']}):")
        print(f"  Array:    {arr}")
        print(f"  Target:   {target}")
        print(f"  Expected index: {expected}")
        print(f"  Result:   {result}")
        print(f"  Status:   {status}\n")