#!/usr/bin/env python3

def my_sort(l):
    l.sort(key=lambda x:x[1])

l = [(1,9),(2,7),(3,11),(4,3),(5,5),(6,9)]
print(l)
my_sort(l)
print(l)
