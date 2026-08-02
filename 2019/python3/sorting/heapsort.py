#!/usr/bin/env python3

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def max_heapify(a, i, heap_size):
    # 0-based child indices
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < heap_size and a[left] > a[largest]:
        largest = left
    if right < heap_size and a[right] > a[largest]:
        largest = right

    if largest != i:
        swap(a, i, largest)
        max_heapify(a, largest, heap_size)

def heapsort(a):
    n = len(a)

    # 1. Build Max Heap (from last non-leaf node down to root)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(a, i, n)

    # 2. Extract elements from heap one by one
    for heap_size in range(n - 1, 0, -1):
        swap(a, 0, heap_size)
        max_heapify(a, 0, heap_size)

def main():
    l = [4, 3, 45, 2, 22, 15, 6, 22, 19, 18, 27]
    heapsort(l)
    print(l)

if __name__ == '__main__':
    main()

