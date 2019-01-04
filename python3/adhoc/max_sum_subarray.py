#!/usr/bin/env python3

import random

def mssa_dp(a):
    n = len(a)
    s = [1] * n
    s[0] = max(a[0], 0)
    max_sum = float('-inf')
    for  i in range(1, n):
        #cur_sum = s[i - 1] + a[i]
        #if (cur_sum < a[i]):
        #    cur_sum = a[i]
        #if (cur_sum < 0):
        #    cur_sum = 0
        #s[i] = cur_sum
        s[i] = max (s[i-1] + a[i], a[i], 0)

        if max_sum < s[i]:
            max_sum = s[i]
    return max_sum


def mid_max(a, st, end):
    mid = int(st + (end - st)/2)

    max_st = mid
    left_sum = 0
    left_max = 0
    #Now determine the start
    for i in range(mid-1, st-1, -1):
        left_sum += a[i]
        if (left_max < left_sum):
            left_max = left_sum
            max_st = i
    #Now determine the end
    max_end = mid
    right_sum = 0
    right_max = 0
    for i in range(mid+1, end+1):
        right_sum += a[i]
        if (right_sum > right_max):
            right_max = right_sum
            max_end = i

    return (left_max+a[mid]+right_max, max_st, max_end)

#In this recursive app, we'll explore the left array for max sum,
#right array for max sum and the 3rd option would be to find the max
#sum including the middle element.
def mssa_rec_dnc(a, st, end):
    # Either st and end are 1 OR
    # st has reached to end or end has become st
    if st == end:
        return a[st], st, end

    if (st > end):
        return 0, -1, -1

    mid = int(st+(end-st)/2)
    left_sum, left_st, left_end    = mssa_rec_dnc(a, st, mid -1)
    right_sum, right_st, right_end = mssa_rec_dnc(a, mid+1, end)
    mid_sum, mid_st, mid_end       = mid_max(a, st, end)

    #Pick max of left, right and middle
    max_sum = left_sum
    max_st = left_st
    max_end = left_end
    if max_sum < right_sum:
        max_sum = right_sum
        max_st = right_st
        max_end = right_end
    if max_sum < mid_sum:
        max_sum = mid_sum
        max_st = mid_st
        max_end = mid_end

    return max_sum, max_st, max_end

# this recursive solution is exactly like finding subarrays in O(n**2)
# way
def mssa_rec11(a, st, end, arrsum):
    if (end == len(a)):
        return arrsum, st, end
    
    leave_sum,s1,e1 = mssa_rec11(a, st+1, end+1, arrsum-a[st]+a[end])
    take_sum,s2,e2  = mssa_rec11(a, st, end+1, arrsum+a[end])
    if (leave_sum > take_sum):
        st = s1
        end = e1
        sum = leave_sum
    else:
        st = s2
        end = e2
        sum = take_sum

    return sum, st, end

#if we want just the max_sum, follow recursive solution is sufficient
def mssa_rec1(a, st, end, arrsum):
    if (end == len(a)):
        return arrsum
    
    return max(mssa_rec1(a, st+1, end+1, arrsum-a[st]+a[end]),
                mssa_rec1(a, st, end+1, arrsum+a[end]))

def mssa_bf(a):
    #n = (int) (20 * random.random())
    #print(n)
    n = len(a)
    print(a)

    max_sum = float('-inf')
    max_sum_st = max_sum_end = 0
    for i in range(n):
        subarr = []
        sum = 0
        for j in range(i, n):
            subarr.append(a[j])
            sum += a[j]
            print(subarr)
        if (sum > max_sum):
            max_list_st = i
            max_list_end = j
            max_sum = sum

    print("max sum:", max_sum, ", list: ", a[max_list_st:max_list_end+1])

def main():
    print("testing max sum subarray")

    #a = [-14, 20, -3, 4, -10]
    #a = [-3, 2, 1, -4, 5]
    #a = [1, -3, 5]
    a = [-3, 5]
    print(a)

    #BF:1
    #mssa_bf(a)

    #App:2
    #arrsum, st, end = mssa_rec11(a, 0, 0, 0)
    #print("max sum (rec11):", arrsum, "list:", a[st:end+1])

    #App:3
    #arrsum = mssa_rec1(a, 0, 0, 0)
    #print("max sum (rec1):", arrsum)

    #App:5
    arrsum, st, end = mssa_rec_dnc(a, 0, len(a) - 1)
    print("st:", st, ", end:", end)
    print("max sum (rec_dnc):", arrsum, a[st:end+1])

    #App:4 DP way, Kadane's
    #arrsum = mssa_dp(a)
    #print("max sum (DP):", arrsum)

main()

