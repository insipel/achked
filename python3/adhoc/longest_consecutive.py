#!/usr/bin/env python3

def find_min_max(l):
    min_l, max_l = l[0], l[0]

    for num in l:
        if num < min_l:
            min_l = num
        elif num > max_l:
            max_l = num

    return max_l, min_l

def lcs(l):
    n = len(l)
    max_l, min_l = find_min_max(l)
    sz = max_l - min_l + 1

    res = [0 for _ in range(sz)]

    for num in l:
        res[num - min_l] = 1

    max_len = float('-inf')
    i = 0

    while i < sz:

        cur_len = 0
        while i < sz and res[i] == 1:
            cur_len += 1
            i += 1

        max_len=max(cur_len, max_len)
        if cur_len == 0:
            i += 1

    print(max_len)

def lcs_leet(nums):
    longest_streak = 0
    num_set = set(nums)

    #print(num_set)
    #for num in num_set:
    for num in nums:

        #print("current num:", num)
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                #print(current_num)

            longest_streak = max(longest_streak, current_streak)
            #print("longest:", longest_streak)

    print(longest_streak)

l = [5, 12, 3, 14, 6, 4]
#l = [100, 4, 200, 1, 3, 2]
#l = [100, 2, 200, 4, 3, 1]
#lcs(l)
lcs_leet(l)

