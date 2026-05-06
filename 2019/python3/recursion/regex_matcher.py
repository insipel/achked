#!/usr/bin/env python3

"""
Given an array of n elements, where each element is at most k positions away from its target position, write an algorithm that sorts in O(n log k) time

Input : arr[] = {6, 5, 3, 2, 8, 10, 9}, k = 3 
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}, k = 4
Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}

import

def ksort(l, k):
    pass

- prepare min heap with first k chars


    cur_idx=-1
    next_elem=k
 loop if next_elem < len(l):
    next_elem+1
    cur_idx+1
  pop min elem, put in cur_idx
   take next elem from input and put in heap
    
    repeat from loop:
        
 if all elements are consumed, then
    keep popping min and put in the result     
 









Write a simple regex verifier. The regex patterns to match are a-z . * 
Where <dot> stands for any character, and 
<star> means the previous  single character 0 or more times. 

The regex must match the entire string, not a substring

input: abaac, abac
pattern: ab*c, a.a*c, .*, .*c, .*d
"""

def regex_matcher(input, pat, i, pidx):
    # i could end, and pidx is at the end: success
    if i == len(input) and pidx == len(pat):
        return True
    
    # i is not at end, pidx is at the end: error
    if i != len(input) and pidx == len(pat):
        return False
    
    # i is at end, pidx is not at the end, -*, -b*, -.*, -b, -.
    if i == len(input) and pidx != len(pat):
        first_p = pat[pidx]
        if pidx+1 == len(pat):
            return False
        
        second_p = pat[pidx+1]
        if second_p == '*':
            regex_matcher(input, pat, i, pidx+2)
    
    
    if input[i] == pat[pidx] or pat[pidx] == '.':
        return regex_matcher(input, pat, i+1, pidx+1)
    elif pat[pidx] == '*':
        prev_p = pat[pidx - 1]
        if input[i] == prev_p or prev_p == '.':
            return regex_matcher(input, pat, i+1, pidx) or regex_matcher(input, pat, i, pidx+1)
        else:
            return regex_matcher(input, pat, i, pidx+1)
    elif input[i] != pat[pidx]:
        return False
    
        
#s = "aabcb"
#p = "aa*.b"
#input: abaac, abac
#pattern: ab*c, a.a*c, .*, .*c, .*d
s="abaac"
#p = "ab*c"
#p = "a.a*c"
p = "a.b*.a*c"
print(regex_matcher(s, p, 0, 0))
