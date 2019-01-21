#!/usr/bin/env python3

from sys import maxint

#Approach1: Brute force way
#space comp: O(n3)
#run time comp: O(n3)
def smatch(string, wordset):
    ans = []
    sstr = get_all_sstrs(string)

    for ss in sstr:
        for char in wordset:
            if char not in ss:
                continue
            ans.append(ss)


    shortest_len = float('inf')
    for answer in ans:
        shortest_len = min(shortest_len, len(answer))

    return shortest_len

def get_all_sstrs(string):
    sstr = []
    temp = ''
    for i in range(len(string)):
        for j in range(i, len(string)):
            sstr.append(string[i:j])
    return sstr

#App2: polynomial time algorithm O(n2)
#has boilerplate algorithm for finding substrings
def smatch(s, p):
    for i in range(len(s)):
        for j in range(i, len(s)):
            pass

maximum_int = maxint
print(maximum_int)
