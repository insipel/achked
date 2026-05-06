#!/usr/bin/env python3

'''
Given a nested list of integers, return the sum of all integers in the
list weighted by their depth.

Each element is either an integer, or a list -- whose elements may
also be integers or other lists.

Different from the previous question where weight is increasing from
root to leaf, now the weight is defined from bottom up. i.e., the leaf
level integers have weight 1, and the root level integers have the
largest weight.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1's at depth 1, one 2 at depth 2.

Example 2:

Input: [1,[4,[6]]]
Output: 17 
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1;
1*3 + 4*2 + 6*1 = 17.
'''

# Instead of multiplying by depth, add integers multiple times (by
# going level by level and adding the unweighted sum to the weighted
# sum after each level).
#
# https://leetcode.com/problems/nested-list-weight-sum-ii/discuss/83641/No-depth-variable-no-multiplication
#
#

def nested(l):
    total_sum = 0; cur_sum = 0
    #depth = 1

    while l:
        nxt_list = []

        for n in l:
            if type(n) == int:
                cur_sum += n # repeating this sum over each level
            else:
                for elem in n:
                    #print("elem:", elem)
                    nxt_list.append(elem)

        total_sum += cur_sum
        l = nxt_list

    return total_sum

l = [[2, [3, 4, [5]]]]
#print(nested(l, 1))
print(nested(l))

