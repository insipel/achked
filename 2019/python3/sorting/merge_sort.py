#!/usr/bin/env python3

def merge(arr, st, m, end):
    # Slice the left and right sorted subarrays
    left = arr[st : m + 1] # exclusive of m+1 indexed element
    right = arr[m + 1 : end + 1]

    i = j = 0
    k = st

    # Merge elements back into arr
    while i < len(left) and j < len(right):
        # If I just have < instead of <=, the stability is destroyed
        # by not picking the left's value before right array value.
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements
    # while i < len(left):
    #     arr[k] = left[i]
    #     i += 1
    #     k += 1

    # while j < len(right):
    #     arr[k] = right[j]
    #     j += 1
    #     k += 1
    
    # instead of the above char by char copy, we can do the following
    # Copy remainders using slice assignment
    arr[k : k + (len(left) - i)] = left[i:]
    # (Optional) If left was exhausted first, copy right's remainders
    k += len(left) - i  # Advance k by the number of elements copied from left
    arr[k : k + (len(right) - j)] = right[j:]

def merge_old(l, st, m, end):
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

def merge_sort(l, st=0, end=None):
    if end is None:
        end = len(l) - 1

    if st < end:
        m = (st + end)//2
        merge_sort(l, st, m)
        merge_sort(l, m+1, end)
        merge(l, st, m, end)
        print(l)


def main():
    l = [3, 6, 19, 2, 14, 22, 9]
    merge_sort(l)
    print(l)

if __name__ == '__main__':
    main()

