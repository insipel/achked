#!/usr/bin/env python3

def missing_elem_xor(a, k):
    n = len(a)

    xor_nums = 0
    for i in range(k+1):
        xor_nums ^= i

    for i in range(n):
        xor_nums = a[i] ^ xor_nums

    print("missing_elem_xor:", xor_nums)

def missing_elem_set(a, k):
    s = set()
    n = len(a)

    for i in range(n):
        s.add(a[i])

    for i in range(1, k+1):
        if i not in s:
            print("missing number:", i)

def missing_elem_bf(a, k):
    n = len(a)

    for i in range(1, k+1):
        found = False;
        for j in range(n):
            if a[j] == i:
                found = True
                break
        if not found:
            print("missing number:", i)
            return

def main():
    print("Running missing element")
    #a = [1, 2, 3, 5, 6]
    #a = [2, 3, 4, 5, 6]
    a = [1, 2, 3, 4, 5]
    k = 6
    #missing_elem_bf(a, k)
    #missing_elem_set(a, k)
    missing_elem_xor(a, k)

main()

