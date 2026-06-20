#!/usr/bin/env python3

# This code implements algorithms to find the k-th smallest element in an
# unsorted list using QuickSelect and heap-based methods.

from heapq import *

# Helper function to swap two elements in a list
def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

# Lomuto partition scheme: partitions the list around a pivot (last element)
# Elements smaller than pivot go to the left, larger to the right
# Returns the final position of the pivot
def partition(l, st, end):
    i = st - 1  # Index for smaller elements
    j = st      # Current index

    # To avoid hitting the worst case in the pathological case of already sorted
    # array, just pick a random pivot
    # pivot_index = random.randint(st, end)
    # swap(l, pivot_index, end)
    # key = l[end]

    # Text diagram at pivot selection:
    #   indexes:  st ...      j ...   end
    #   values:  [.....|.........| current | ... | pivot ]
    #          < key   ^          ^        ^
    #                  |   > key  |        |
    #                  i          j      key/end
    # key is chosen as the element at `end`; `i` marks the last smaller element;
    # `j` scans the current window up to `end - 1`.
    key = l[end]  # Pivot element

    while j < end:
        if l[j] < key:
            i += 1
            swap(l, i, j)  # Swap to place smaller element on left
        j += 1

    i += 1
    swap(l, i, end)  # Place pivot in its correct position
    return i

# QuickSelect algorithm to find the k-th smallest element (0-based index)
# Uses partitioning to narrow down the search space
def kth_rank_quickSelect(l, k):
    n = len(l)
    if k > n:
        return -1  # Invalid k
    st = 0        # Start index
    end = n - 1   # End index
    j = -1        # Partition index

    while j != k:
        j = partition(l, st, end)  # Partition and get pivot position

        if j < k:
            st = j + 1  # Search in right half
        else:
            end = j - 1  # Search in left half

    return l[k]  # k-th element is now at index k

# Alternative method using a min-heap to find the k-th smallest element
# Builds a heap and pops k times to get the k-th element
def kth_rank_2(l, k):
    heap = [c for c in l]  # Copy the list
    n = len(l)

    heapify(heap)  # Convert to min-heap

    for _ in range(k):
        item = heappop(heap)  # Pop the smallest element k times
    return item

# Main function to test the algorithms
def main():
    l = [4, 19, 6, 14, 29, 8, 12, 23]  # Sample list
    k = 20  # Find the 20th smallest (but list has only 8 elements)
    if k > len(l):
        print(f"Error: Array size {len(l)} is out of range for kth: {k} element")
        return
    print("build_heap method:", kth_rank_2(l, k))  # Commented out heap method
    print("quick_select method:", kth_rank_quickSelect(l, k - 1))  # k-1 for 0-based index

if __name__ == '__main__':
    main()

