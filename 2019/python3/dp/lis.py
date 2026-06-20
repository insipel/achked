#!/usr/bin/env python3

# Longest Increasing Subsequence

def lis(l):
    n = len(l)

    # res will hold the length of the LIS starting at idx i
    res = [1 for _ in range(n)]
    # lis will hold the index of the next element. if it's same as the
    # current element's index, then the end has reached.
    lis = [0 for _ in range(n)]

    #Base case: last element
    res[n-1] = 1
    lis[n-1] = n - 1

    for i in range(n-2, -1, -1):
        temp_max = 0
        res_idx = i
        for j in range(i+1, n):
            if l[i] < l[j] and res[j] >= temp_max:
                temp_max = res[j]
                res_idx = j
        res[i] = temp_max + 1
        lis[i] = res_idx

    print(res)
    print(lis)
    return(res[0])

def main():
    l = [13, 5, 9, 23, 6, 8, 16]
    #l = [13, 9, 8, 6]
    #l = [1, 9, 18, 26]
    print(lis(l))

if __name__ == '__main__':
    main()

