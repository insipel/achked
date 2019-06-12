#!/usr/bin/env python3

def merge(l, st, m, end):
    print("st:", st, ", m:", m, ", end:", end)
    n1 = m - st + 1
    n2 = end - m
    l1 = [0] * n1
    l2 = [0] * n2

    for i in range(n1):
        l1[i] = l[st + i]
    for i in range(n2):
        l2[i] = l[m + i + 1]

    i, j, k = 0, 0, st

#    while k < end:
#        if i < n1 and j < n2 and l1[i] <= l2[j]:
#            # There is a bug here that even if elements are left in
#            # l1 but none in l2, it won't get copied to the dest array
#            # due to j < n2 condition.
#            l[k] = l1[i]
#            i += 1
#        elif j < n2:
#            l[k] = l2[j]
#            j += 1
#        k += 1
    while i < n1 and j < n2:
        if l1[i] <= l2[j]:
            l[k] = l1[i]
            i += 1
        else:
            l[k] = l2[j]
            j += 1
        k += 1

    while i < n1:
        l[k] = l1[i]
        k += 1
        i += 1

    while j < n2:
        l[k] = l2[j]
        k += 1
        j += 1

def merge_sort(l, st, end):
    if st < end:
        m = (st + end)//2
        merge_sort(l, st, m)
        merge_sort(l, m+1, end)
        merge(l, st, m, end)
        print(l)


def main():
    l = [3, 6, 19, 2, 14, 22, 9]
    merge_sort(l, 0, len(l) - 1)
    print(l)

if __name__ == '__main__':
    main()

