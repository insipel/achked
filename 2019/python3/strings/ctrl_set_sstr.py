#!/usr/bin/env python3

# Problem: Given a string and a set of characters, find the length of the shortest
# substring that contains all the characters in the set (at least once).

# Note: In Python 3, sys.maxint does not exist (integers are unbounded).
# Use float('inf') for infinity instead.

# Approach1: Brute force way
# space comp: O(n3)
# run time comp: O(n3)
def smatch1(string, wordset):
    ans = []
    sstr = get_all_sstrs(string)

    for ss in sstr:
        found = True
        for char in wordset:
            if char not in ss:
                found = False
                break
        if found:
            print(f"Found in {ss}")
            ans.append(ss)

    shortest_len = float("inf")
    for answer in ans:
        shortest_len = min(shortest_len, len(answer))
        # print(f"Found: {shortest_len} ")

    return shortest_len


def get_all_sstrs(string):
    sstr = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            # Fix: j from i+1 to len(string) to include full substrings ending
            # at the string's end also, len(string) + 1 is to generate the end
            # index since it's exclusive. If we don't have + 1, the end idex
            # will be 1 less and
            # since it's exclusive, the last char will be left out from substr
            # generation.
            sstr.append(string[i:j])
    print(f"sstr: {sstr}")  # Uncomment to debug: prints all substrings (O(n^2) output)
    return sstr


# App2: polynomial time algorithm O(n2)
# has boilerplate algorithm for finding substrings
def smatch(s, p):
    for i in range(len(s)):
        for j in range(i, len(s)):
            pass


smatch1("animeshpathakisgoing", "meshet")
