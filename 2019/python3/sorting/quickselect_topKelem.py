'''
To find the top \(k\) largest elements, we can adapt Quickselect to
partially sort the array. Instead of searching for the \(k\)-th
smallest item, we look for the element at index len(arr) - k.
Once Quickselect places the pivot at that exact index, every
element to its right is guaranteed to be greater than or equal
to it. This gives us the \(k\) largest elements in
\(\mathcal{O}(n)\) average time. Here is the Python
implementation.
'''
import random

def top_k_largest(arr, k):
    """
    Returns the top k largest elements from the array.
    The returned elements are not guaranteed to be sorted among themselves.
    """
    n = len(arr)
    if k <= 0:
        return []
    if k >= n:
        return arr.copy() # Return copy of full array if k matches/exceeds size
        
    # The target index that splits the top k largest elements to the right
    target_index = n - k
    
    # Run Quickselect to position the correct pivot at target_index
    quickselect_slice(arr, 0, n - 1, target_index)
    
    # Everything from target_index to the end is part of the top k elements
    return arr[target_index:]

def quickselect_slice(arr, low, high, target):
    """Helper that runs quickselect recursively until the target index is found."""
    if low >= high:
        return
        
    pivot_index = randomized_partition(arr, low, high)
    
    if pivot_index == target:
        return
    elif pivot_index > target:
        quickselect_slice(arr, low, pivot_index - 1, target)
    else:
        quickselect_slice(arr, pivot_index + 1, high, target)

def randomized_partition(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[rand_pivot], arr[high] = arr[high], arr[rand_pivot]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
nums = [3, 2, 1, 5, 6, 4, 9, 7, 8]
k = 3
result = top_k_largest(nums, k)
print(f"The top {k} largest elements are: {result}")
# Expected output: [7, 8, 9] (order inside the slice may vary)
