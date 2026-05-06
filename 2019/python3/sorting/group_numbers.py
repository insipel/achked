#!/usr/bin/env python3

# This code groups numbers in a list by partitioning them into even numbers on
# the left and odd numbers on the right.

def group(a):
    n = len(a)
    l, r = 0, n - 1
    i = 0

    while l < r:

        if a[i] % 2 == 0:
            l += 1
            i += 1
        else:
            a[i], a[r] = a[r], a[i]
            r -= 1

    print(a)

a = [3, 2, 5, 9, 8, 4, 6]
group(a)

