#!/usr/bin/env python3

def insertion_sort(l):

    for i in range(len(l)):
        key = l[i]
        j = i
        while j > 0:
            if l[j - 1] > key:
                l[j] = l[j - 1]
                j -= 1
            else:
                break
        l[j] = key

def insertion_sort_new(arr):
    """
    Sorts an array in ascending order using the Insertion Sort algorithm.
    
    Algorithm Explanation:
    ----------------------
    Insertion sort works similarly to how people sort playing cards in their hands.
    - The array is virtually split into a sorted and an unsorted part.
    - Values from the unsorted part are picked and placed into the correct
      position in the sorted part.
      
    Complexity:
    -----------
    - Time Complexity:
        - Best Case: O(N) when the array is already sorted.
        - Average Case: O(N^2)
        - Worst Case: O(N^2) when the array is sorted in reverse order.
    - Space Complexity: O(1) auxiliary space (In-place algorithm).
    """
    # Traverse through 1 to len(arr)
    # Element at index 0 is considered trivially sorted initially
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be positioned
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1
            
        # Insert the key into its correct sorted position
        arr[j + 1] = key
        
    return arr


# -------------------------------------------------------------------
# Test Cases & Demonstration
# -------------------------------------------------------------------
if __name__ == "__main__":
    l = [4, 3, 45, 2, 22, 15, 6, 22, 19, 18, 27]
    insertion_sort(l)
    print(l)

    test_cases = [
        {"name": "Unsorted Array", "input": [12, 11, 13, 5, 6]},
        {"name": "Already Sorted Array", "input": [1, 2, 3, 4, 5]},
        {"name": "Reverse Sorted Array", "input": [9, 7, 5, 3, 1]},
        {"name": "Array with Duplicates", "input": [4, 2, 4, 3, 2, 1]},
        {"name": "Single Element Array", "input": [42]},
        {"name": "Empty Array", "input": []}
    ]

    print("=== Running Insertion Sort Tests ===\n")
    for test in test_cases:
        # Create a copy so we don't modify original list before printing
        original = list(test["input"])
        sorted_arr = insertion_sort_new(original)
        
        print(f"Test: {test['name']}")
        print(f"  Input : {test['input']}")
        print(f"  Output: {sorted_arr}\n")
