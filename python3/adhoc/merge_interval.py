#!/usr/bin/env python3

from operator import itemgetter

def getMergedIntervals(a1):
    #
    # Write your code here.
    #
    #a = sorted(a1, key=itemgetter(0))
    a = sorted(a1, key=lambda x: x[0])
    #print(a)
    st, end = a[0]
    op = []
    for st1, end1 in a[1:]:
        
        if st1 <= end:
            end = max(end1, end)
        else:
            op.append([st,end])
            st = st1
            end = end1
    
    op.append([st,end])
    
    return op

def main():
    print("Finding merge interval")
    #a = [[10, 12], [1, 2], [1000, 100000], [-1000000000, 1000000000], [2, 5], [7, 10], [123, 456]]
    a = [[20, 30], [4, 30], [40, 43], [10, 30], [3, 30]]
    print(getMergedIntervals(a))

main()

