#!/usr/bin/env python3

def my_sort(l):
    l.sort(key=lambda x:x[1])

l = [(1,9),(2,7),(3,11),(4,3),(5,5),(6,9)]
print(l)
# l_without_lambda = l.sort() # sorts in place and changes l; sorted() is the work around
print(f"Without lambda sort: {sorted(l)}")
print(f"With lambda sort: {sorted(l, key=lambda x: x[1])}")
my_sort(l)
print(l)
