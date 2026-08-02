import random

def quickselect(arr, k):
    """
    Returns the k-th smallest element (0-indexed) in the array.
    k=0 gives the minimum element, k=len(arr)-1 gives the maximum.
    """
    if not arr or k < 0 or k >= len(arr):
        raise ValueError(f"Index k={k} out of bounds for array of length"
        f":{len(arr) if arr else 0}. Array provided: {arr}")
        
    quickselect_helper(arr, 0, len(arr) - 1, k)
    return arr[k]

def quickselect_helper(arr, low, high, k):
    # Base case: if the array contains only one element
    if low == high:
        return
        
    # Partition the array around a random pivot
    pivot_index = randomized_partition(arr, low, high)
    
    # If the pivot is at the target position k
    if pivot_index == k:
        return
    # If target k is smaller, search the left sub-array
    elif pivot_index > k:
        quickselect_helper(arr, low, pivot_index - 1, k)
    # If target k is larger, search the right sub-array
    else:
        quickselect_helper(arr, pivot_index + 1, high, k)

def randomized_partition(arr, low, high):
    """Selects a random pivot, swaps it to the end, and partitions."""
    rand_pivot = random.randint(low, high)
    arr[rand_pivot], arr[high] = arr[high], arr[rand_pivot]
    return partition(arr, low, high)

def partition(arr, low, high):
    """Standard in-place partition using the last element as the pivot."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
# Finding the 3rd smallest element (index 2: 0-indexed)
nums = [7, 10, 4, 3, 20, 15]
target_k = 2

result = quickselect(nums, target_k)
print(f"The {target_k}-indexed smallest element is: {result}") 
# Sorted version would be, so index 2 is 7.
