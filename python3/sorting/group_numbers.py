#!/usr/bin/env python3

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

