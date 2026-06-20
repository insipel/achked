#!/usr/bin/env python3

def alternate(l):
    n = len(l)
    pi, ni = 0, 0
    pos_list = [0] * n
    neg_list = [0] * n

    for i in range(n):
        if l[i] >= 0:
            pos_list[pi] = l[i]
            pi += 1
        else:
            neg_list[ni] = l[i]
            ni += 1

    i, j, k = 0, 0, 0

    while i < pi and j < ni:
        l[k] = pos_list[i]
        i += 1
        l[k+1] = neg_list[j]
        j += 1

        k += 2

    while i < pi:
        l[k] = pos_list[i]
        i += 1
        k += 1

    while j < ni:
        l[k] = neg_list[j]
        j += 1
        k += 1

    print(l)

#l = [1, 3, 6, -2, -9, -1, 5, 8, -6]
l = [1, 3, 6, -2, 5, 8, -6]
print(l)
alternate(l)

