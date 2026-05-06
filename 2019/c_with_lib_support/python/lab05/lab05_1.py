#!/usr/bin/env python
""" Lab 05 01 excercise """

import sys

def GetInput():
    print "Enter your input: "
    text = sys.stdin.readline()
    return text

def CountVowels():
    text = GetInput()
    print "Input str: %s" % text

    count = 0
    for ch in text:
        if ch in 'aeiouAEIOU':
            count += 1

    print "THere are %d vowels in this text" % count

if __name__ == '__main__':
    CountVowels()

