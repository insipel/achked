#!/usr/bin/env python3

import math

def sqrt1(x):
    if x == 0:
        return x

    left = 1; right = x

    while (True):
        mid = (left + right) / 2;
        if (mid > x / mid):
            right = mid - 1
        elif (mid + 1 > x / (mid + 1)): #//mid &lt; x / mid
            return mid
        else: #//mid &lt; x / mid
            left = mid + 1

def sqrt2(num):

    if num<0:
        raise ValueError

    if num==1:
        return 1

    low=0
    # This basically means to start with the range as 0 to n/2+delta.
    # The delta can be a small bit higher than half. If we choose 1 or
    # 0.1, the result should be similar.
    #high=1+(num/2)
    high=0.1+(num/2)

    while low < high:

        mid=low+(high-low)/2
        square=mid**2

        print(square)
        if abs(square - num) < 0.000005:
            return mid

        elif square<num:
            low=mid

        else:
            high=mid

    return low

print(sqrt1(2))
print(math.sqrt(5), sqrt2(5))

