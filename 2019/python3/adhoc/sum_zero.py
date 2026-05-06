#!/usr/bin/env python3

# the idea in the linear time algorithm is that we keep on
# accumulating the sum and use that to calculate the sum in the
# different subarrays.
# When we check if the sum exists in the hash, we are checking to find
# the subarray which contains the sum zero. eg. sum at index 2
# contains sum of elems 0 to 2. Later at an index say 5 we see the sum
# match sum[2], then we know that the subarray 3-5 contains sum zero.
# sum from elements 3, 4 and 5 is 0.
#
# Complete the sumZero function below.
def sumZero(a):
    
    #n = len(a)
    sum = 0
    sum_map = {}
    res = [None] * 2
    
    for i in range(len(a)):
        if not a[i]:
            res[0] = i
            res[1] = i
            return res
        else:
            sum += a[i]
            if sum in sum_map:
                res[0] = sum_map[sum] + 1
                res[1] = i
                return res
            elif not sum:
                res[0] = 0
                res[1] = i
                return res
            sum_map[sum] = i
    res[0] = -1            
    return res

def sumZero_brute(arr):
    n = len(arr)
    for i in range(n):
        total = arr[i]
        
        if not total:
            return [i, i]
            
        for j in range(i+1, n):
            total += arr[j]
            
            if not total:
                return [i, j]
    return [-1]

def sumZero1(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        total = arr[i]
        
        #print("i:", i, " total:", total)
        if not total:
            return [i, i]
            
        for j in range(i+1, n):
            total += arr[j]
            
            #print("i:", i, " j:", j, " total:", total)
            if not total:
                return [i, j]
    return [-1]

def main():
    print("running sum zero")
    #a = [6,5,1,2,-3,7,-4]
    a = [1, 0, -1]
    #a = [4, 4, 4, 4, -16]
    #a = [-1, -2, 0, 3]
    print(sumZero(a))

main()

