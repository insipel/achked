#!/usr/bin/env python3

def second_smallest(A):
    cur = 0
    potential = float('inf')

    while cur < len(A):
        l = left(cur)
        r = right(cur)

        if A[l] == A[cur]:
            equal_node = l
            other_node = r
        else:
            equal_node = r
            other_node = l

        if potential > a[other_node]:
            potential = a[other_node]

        cur = equal_node

    return potential

def left(i):
    return (2 * i + 1)

def right(i):
    return (2 * i + 2)

def build(A):
    n = len(A)
    h = int(ceil(log2(n)))
    nleafs = int(pow(2, h))
    total_n = 2 * nleafs - 1 # n leaves and n-1 internal nodes
    L = [0] * total_n
    construct(A, 0, n-1, 0, L)

    actual_elems = 2 * n - 1
    return L, actual_elems

def construct(A, st, end, idx, L):

    if st == end:
        L[idx] = A[st]
        return A[st]

    m = int((st+end)/2)
    lidx = left(idx)
    ridx = right(idx)

    L[lidx] = construct(A, st, m, lidx, L)
    L[ridx] = construct(A, m+1, end, ridx, L)
    return L[idx]


