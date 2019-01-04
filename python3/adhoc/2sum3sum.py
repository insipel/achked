#!/usr/bin/env python3

def find_2sum_set_mod(a, k):
    s = set()
    n = len(a)

    l = []
    for i in range(n):
        if (k-a[i]) in s:
            l.append((k-a[i], a[i]))
        s.add(a[i])
    return l

def find_2sum_sorted_mod(a, target):
    n = len(a)
    a = sorted(a)

    left = 0
    right = n - 1
    
    l = []
    while (left < right):
        cur_sum = a[left] + a[right]
        if cur_sum == target:
            l.append((a[left], a[right]))
            left += 1
        elif cur_sum < target:
            left += 1
        else:
            right -= 1
    return l

def find_2sum_sorted(a, target):
    n = len(a)
    a = sorted(a)

    left = 0
    right = n - 1
    
    while (left < right):
        cur_sum = a[left] + a[right]
        if cur_sum == target:
            print("find_2sum_sorted: num:", a[left], a[right])
            left += 1
        elif cur_sum < target:
            left += 1
        else:
            right -= 1

def find_2sum_set(a, k):
    s = set()
    n = len(a)

    for i in range(n):
        if (k-a[i]) in s:
            print("find_2sum_set: nums:", a[i], k-a[i])
        s.add(a[i]) # this addition has to happend after lookup

def find_2sum_orig(a, k):
    n = len(a)

    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] == k:
                print("find_2sum_orig: nums:", a[i], a[j])

#This is not 2sum solution, instead it is subarray sum problem. It
#prints the subarray whose sum is a given one. If the sum is of
#disjoint elements, this fails. 1,2,3,4,5 and sum 6
def find_2sum(a, k):
    n = len(a)

    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += a[j]
            if (sum == k):
                print("Found sum: list[]-", a[i:j+1])

def find_3sum_sorted(a, target):
    n = len(a)
    a = sorted(a)

    for i in range(n):
        l = find_2sum_sorted_mod(a[i+1:], target-a[i])

        if l:
            for aj, ak in l:
                print("find_3sum_sorted: nums:", a[i], aj, ak)

def find_3sum_set(a, target):
    n = len(a)

    for i in range(n):
        l = find_2sum_set_mod(a[i+1:], target-a[i])

        if len(l):
                for aj, ak in l:
                    print("find_3sum_set: nums:", a[i], aj, ak)

def find_3sum_orig(a, target):
    n = len(a)

    for i in range(n):
        sum = a[i]
        for j in range(i+1, n):
            sum = a[i] + a[j]  ## Had a bug here: sum += a[j]
                               ## sum would accumulate a[j]
            for k in range(j+1, n):
                if sum + a[k] == target:
                    print("find_3sum_orig: nums:", a[i], a[j], a[k])

def main():
    print("Running 2 sum problem")
    a = [2, 1, 3, 4, 5]
    k = 10
    #find_2sum_orig(a, k)
    #find_2sum_set(a, k)
    #find_2sum_sorted(a, k)

    #find_3sum_orig(a,k)
    #find_3sum_set(a,k)
    find_3sum_sorted(a,k)

main()

