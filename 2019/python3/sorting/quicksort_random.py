import random

def quicksort_random(arr, low=0, high=None):
    """Sorts an array in-place using Randomized Quicksort."""
    if high is None:
        high = len(arr) - 1
        
    if low < high:
        # Partition the array using a random pivot
        pivot_index = randomized_partition(arr, low, high)
        
        # Recursively sort the sub-arrays
        quicksort_random(arr, low, pivot_index - 1)
        quicksort_random(arr, pivot_index + 1, high)
    return arr

def randomized_partition(arr, low, high):
    """Selects a random pivot, swaps it to the end, and partitions."""
    # Pick a random index between low and high (inclusive)
    rand_pivot = random.randint(low, high)
    
    # Swap the random pivot element with the last element
    arr[rand_pivot], arr[high] = arr[high], arr[rand_pivot]
    
    # Delegate to the standard partitioning logic
    return partition(arr, low, high)

def partition(arr, low, high):
    """Standard partition using the last element as the pivot."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
nums = [3, 6, 8, 10, 1, 2, 1]
print("Original:", nums)
quicksort_random(nums)
print("Sorted:  ", nums)
