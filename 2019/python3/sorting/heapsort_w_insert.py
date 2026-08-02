#!/usr/bin/env python3

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def max_heapify(a, i, sz):
    """Sifts down element at index i to maintain the max-heap property."""
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < sz and a[left] > a[largest]:
        largest = left
    if right < sz and a[right] > a[largest]:
        largest = right

    if largest != i:
        swap(a, i, largest)
        max_heapify(a, largest, sz)

def build_max_heap(a):
    """Converts an unsorted array into a Max-Heap in O(N) time."""
    sz = len(a)
    for i in range(sz // 2 - 1, -1, -1):
        max_heapify(a, i, sz)

def heapify_up(a, i):
    """Sifts up element at index i to maintain the max-heap property after insertion."""
    while i > 0:
        parent = (i - 1) // 2 # Note the (i - 1) part here
        if a[i] > a[parent]:
            swap(a, i, parent)
            i = parent
        else:
            break

def insert_max_heap(a, key):
    """Inserts a new element into an existing Max-Heap in O(log N) time."""
    a.append(key)
    heapify_up(a, len(a) - 1)

def heapsort(a):
    """Sorts an array in ascending order in-place using Heapsort in O(N log N) time."""
    # Step 1: Build a Max-Heap from the input array
    build_max_heap(a)

    # Step 2: Extract the maximum element repeatedly and reduce heap size
    for sz in range(len(a) - 1, 0, -1):
        swap(a, 0, sz)          # Move current max to the end
        max_heapify(a, 0, sz)   # Restore max-heap on the remaining reduced heap

def heapsort_existing_heap(a):
    """
    Sorts an array that is ALREADY a valid max-heap.
    Skips the build_max_heap step and goes straight to extraction.
    """
    for sz in range(len(a) - 1, 0, -1):
        swap(a, 0, sz)          # Swap root (max value) to the end
        max_heapify(a, 0, sz)   # Re-heapify the remaining heap

def main():
    # -------------------------------------------------------------
    # Demo 1: Building a Max-Heap and Inserting Elements
    # -------------------------------------------------------------
    heap_list = [4, 3, 45, 2, 22, 15, 6, 22, 19, 18, 27]
    print("Original List:               ", heap_list)

    build_max_heap(heap_list)
    print("After build_max_heap:        ", heap_list)

    insert_max_heap(heap_list, 10)
    print("After insert_max_heap(10):   ", heap_list)

    # Step 3: Perform heapsort
    # Since heap_list is ALREADY a valid max-heap, we can extract elements directly
    heapsort_existing_heap(heap_list)
    print("After heapsort:              ", heap_list)

    print("-" * 60)

    # -------------------------------------------------------------
    # Demo 2: Standard Heapsort (Sorting an array)
    # -------------------------------------------------------------
    sort_list = [4, 3, 45, 2, 22, 15, 6, 22, 19, 18, 27]
    heapsort(sort_list)
    print("Sorted List via heapsort():  ", sort_list)

if __name__ == '__main__':
    main()