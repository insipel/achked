#!/usr/bin/env python3

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def max_heapify(a, i, sz):
    left = 2 * i 
    right = 2 * i + 1

    if left < sz and a[i] < a[left]:
        largest = left
    else:
        largest = i

    if right < sz and a[right] > a[largest]:
        largest = right

    if i != largest:
        swap(a, i, largest)
        max_heapify(a, largest, sz)

def heapsort(a):
    sz = len(a)
    # we can go from sz//2 to 0 or sz to 0, it doesn't matter since
    # the guard conditions are protecting the largest check.
    for i in range(sz//2, -1, -1):
        max_heapify(a, i, sz)

    for sz in range(len(a) - 1, -1, -1):
        # following is an optimization
        #if a[0] > a[sz]:
            swap(a, 0, sz)
            max_heapify(a, 0, sz - 1)

def main():
    l = [4, 3, 45, 2, 22, 15, 6, 22, 19, 18, 27]
    heapsort(l)
    print(l)

if __name__ == '__main__':
    main()

