#!/usr/bin/env python3

'''
Given a nested list of integers, return the sum of all integers in the
list weighted by their depth.

Each element is either an integer, or a list -- whose elements may
also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.

Example 2:

Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3;
1 + 4*2 + 6*3 = 27.

Visualize this problem as a n-ary Tree problem

L-0:           root
L-1:    [1, 1]   2    [1,1]
L-2: 1   1             1   1

L-0:          root [[1,[4,[6]]]]
L-1:    1              [4, [6]]
L-2:                  4    [6]
L-3:                       6

'''

def nested(l, depth):
    sum = 0

    for n in l:
        sum += nested(n, depth+1)

        if type(n) == int:
            sum += n * depth
        else:
            sum += nested(n, depth+1)

    return sum

l = [[2, [3, 4, [5]]]]
print(nested(l, 1))

