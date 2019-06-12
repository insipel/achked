#!/usr/bin/env python3

from heapq import *

def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def partition(l, st, end):
    i = st - 1
    j = st
    key = l[end]

    while j < end:
        if l[j] < key:
            i += 1
            swap(l, i, j)
        j += 1

    i += 1
    swap(l, i, end)
    return i

def kth_rank_quickSelect(l, k):
    n = len(l)
    if k > n:
        return -1
    st = 0
    end = n - 1
    j = -1

    while j != k:
        j = partition(l, st, end)

        if j < k:
            st = j + 1
        else:
            end = j - 1

    return l[k]

def kth_rank_2(l, k):
    heap = [c for c in l]
    n = len(l)

    heapify(heap)

    for _ in range(k):
        item = heappop(heap)
    return item

def main():
    l = [ 4, 19, 6, 14, 29, 8, 12, 23]
    k = 1
    #print("build_heap method:", kth_rank_2(l, k))
    print("quick_select method:", kth_rank_quickSelect(l, k - 1))

if __name__ == '__main__':
    main()

