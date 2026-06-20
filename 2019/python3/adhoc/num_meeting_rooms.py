#!/usr/bin/env python3

from operator import itemgetter
from heapq import *

#def getMergedIntervals(a1):
def num_meeting_rooms(a1):
    a = sorted(a1, key=lambda x: x[0])
    print(a)
    min_heap = []

    count = 0
    for st1, end1 in a:
        if not min_heap:
            heappush(min_heap, (st1, end1))
            count +=1
        else:
            top_st, top_end = min_heap[0]

            if top_end > st1:
                count += 1
            heappush(min_heap, (st1, end1))
    
    print("number of rooms:", count)
    return count

def main():
    print("Finding number of meeting rooms")
    #a = [[20, 30], [4, 30], [40, 43], [10, 30], [3, 30]]
    a = [(1, 4), (5, 6), (8, 9), (2, 6)]
    print(num_meeting_rooms(a))

main()

