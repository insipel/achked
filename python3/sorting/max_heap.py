#!/usr/bin/env python3

from heapq import *

class max_heap1():
    def __init__(self):
        self.l = []
    def heappush(self, item):
        heappush(self.l, -item)
    def heappop(self):
        x = heappop(self.l)
        return -x
    def heapsize(self):
        return len(self.l)
    def heappeek(self):
        return -self.l[0]


class max_heap():
    def __init__(self):
        self.heap = []
    def heappush(self, x):
        heappush(self.heap, -x)
    def heappop(self):
        x = heappop(self.heap)
        return -x
    def heappeek(self):
        return -self.heap[0]
    def heapsize(self):
        return len(self.heap)
    

#m1 = max_heap()
#m1.heappush(34)
#m1.heappush(7)
#m1.heappush(31)
#print(m1.heappeek())
#m1.heappush(44)
#print(m1.heappeek())
#m1.heappop()
#print(m1.heappeek())
#m1.heappop()
#print(m1.heappeek())
#m1.heappop()
#print(m1.heappeek())

m2 = max_heap1()
m2.heappush(24)
m2.heappush(17)
m2.heappush(11)
#print(m1.heappeek())
#m1.heappush(44)
#print(m1.heappeek())
#m1.heappop()
#print(m1.heappeek())
#m1.heappop()
#print(m1.heappeek())
#m1.heappop()
print(m2.heappeek())

'''
class MaxHeapObj(object):
  def __init__(self,val): self.val = val
  #def __lt__(self,other): return self.val > other.val
  def __lt__(self,other): return self.val > other.val
  def __eq__(self,other): return self.val == other.val
  def __str__(self): return str(self.val)

#maxh = []
#heapq.heappush(maxh,MaxHeapObj(x))
#x = maxh[0].val # fetch max value
#x = heapq.heappop(maxh).val # pop max value
#
class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self,x): heapq.heappush(self.h,x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self,i): return self.h[i]
  def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
  def heappush(self,x): heapq.heappush(self.h,MaxHeapObj(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self,i): return self.h[i].val

#Example usage:
#
#minh = MinHeap()
maxh = MaxHeap()
# add some values
#minh.heappush(12)
maxh.heappush(12)
#minh.heappush(4)
maxh.heappush(4)
# fetch "top" values
#print(minh[0],maxh[0]) # "4 12"
print(maxh[0]) # "4 12"
# fetch and remove "top" values
#print(minh.heappop(),maxh.heappop()) # "4 12"
print(maxh.heappop()) # "4 12"
print(maxh.heappop()) # "4 12"
'''

