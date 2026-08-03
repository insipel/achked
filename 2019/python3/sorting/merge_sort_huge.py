def merge_sort_huge(arr):
    if not arr:
        return
    # Allocate a single auxiliary buffer once upfront
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

    # Merge into arr
    while i <= m and j <= end:
        if buffer[i] <= buffer[j]:
            arr[k] = buffer[i]
            i += 1
        else:
            arr[k] = buffer[j]
            j += 1
        k += 1

    # Only copy remaining elements from left side.
    # Right-side elements are already in arr[k..end] in sorted order!
    while i <= m:
        arr[k] = buffer[i]
        i += 1
        k += 1


l = [3, 6, 19, 2, 14, 22, 9]
merge_sort_huge(l)
print(l)  # Output: [2, 3, 6, 9, 14, 19, 22]