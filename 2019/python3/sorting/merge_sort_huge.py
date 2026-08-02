# Ultimate Optimization for Huge Lists (Single Aux Buffer)
#
# If you are sorting a very large list in Python using Merge
# Sort and want maximum efficiency in both memory and speed,
# the standard industrial approach is to allocate a single
# auxiliary buffer of size N upfront.This eliminates
# repeated list allocations altogether:

def merge_sort_huge(arr):
    # Allocate a single auxiliary buffer array once upfront
    buffer = [None] * len(arr)
    _merge_sort_helper(arr, buffer, 0, len(arr) - 1)


def _merge_sort_helper(arr, buffer, st, end):
    if st >= end:
        return

    m = (st + end) // 2
    _merge_sort_helper(arr, buffer, st, m)
    _merge_sort_helper(arr, buffer, m + 1, end)
    _merge(arr, buffer, st, m, end)


def _merge(arr, buffer, st, m, end):
    # Copy segment to buffer
    for i in range(st, end + 1):
        buffer[i] = arr[i]

    i, j, k = st, m + 1, st

    while i <= m and j <= end:
        if buffer[i] <= buffer[j]:
            arr[k] = buffer[i]
            i += 1
        else:
            arr[k] = buffer[j]
            j += 1
        k += 1

    # while i <= m:
    #     arr[k] = buffer[i]
    #     i += 1
    #     k += 1
    # while j <= end:
    #     arr[k] = buffer[j]
    #     j += 1
    #     k += 1
    # Copy remaining elements from left side (if any)
    if i <= m:
        arr[k : k + (m - i + 1)] = buffer[i : m + 1]

    # Copy remaining elements from right side (if any)
    if j <= end:
        arr[k : k + (end - j + 1)] = buffer[j : end + 1]

l = [3, 6, 19, 2, 14, 22, 9]
# does in place sorting.
merge_sort_huge(l)
print(l)