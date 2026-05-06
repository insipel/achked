#!/usr/bin/env python3

import queue as queue
from heapq import *

prio_queue = queue.PriorityQueue()
prio_queue.put((2, 8, 'super blah'))
prio_queue.put((1, 4, 'Some thing'))
prio_queue.put((1, 3, 'This thing would come after Some Thing if we sorted by this text entry'))
prio_queue.put((5, 1, 'blah'))

while not prio_queue.empty():
    item = prio_queue.get()
    print('%s.%s - %s' % item)

pq = []
event_finder = {}

def add_event(label, prio):
    if label in event_finder:
        remove_event(label)

    entry = [prio, label]
    event_finder[label] = entry
    heappush(pq, entry)

def remove_event(label):
    entry = event_finder[label]
    event_finder.pop(label)

    last = pq[-1]
    entry[0] = last[0]
    entry[1] = last[1]
    pq.pop(-1)
    heapify(pq)
    
# updates the priority for an existing label
def update_event(label, prio):
    if label in event_finder:
        remove_event(label)
        #print("after remove:", pq)
    add_event(label, prio)
    #heappush(pq, entry)

#        Label and Priority
add_event(3, 0)
add_event(1, 9)
add_event(5, 3)
add_event(6, 1)
add_event(7, 8)
add_event(7, 2)
print(pq)
print(event_finder)
update_event(5, 15)
#add_event(5, 15)
print(pq)
print(event_finder)
print("===============")

while pq:
    print(pq)
    prio, label = pq[0]
    print(prio, label)
    heappop(pq)




pq = []
heappush(pq, [0, 3])
heappush(pq, [2, 5])
heappush(pq, [1, 4])
heappush(pq, [4, 7])
heappush(pq, [3, 6])
print(pq)
heappush(pq, [3, 16])
heappush(pq, [2, 12])
print(pq)
