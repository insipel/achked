def quicksort(arr, low=0, high=None):
    """Sorts an array in-place using the Quicksort algorithm."""
    if high is None:
        high = len(arr) - 1
        
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
    return arr

def partition(arr, low, high):
    """Partitions the array using the last element as the pivot."""
    pivot = arr[high]
    i = low - 1  # Index of the smaller element
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]   # Swap elements
            
    # Swap the pivot element with the greater element at i + 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
nums = [64, 34, 25, 12, 22, 11, 90]
print("Original:", nums)
quicksort(nums)
print("Sorted:  ", nums)
