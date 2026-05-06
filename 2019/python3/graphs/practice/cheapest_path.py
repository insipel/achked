#!/usr/bin/env python3

from heapq import *

pq = []

# Doesn't work on node address. key is node.data
event_finder = {}

def add_event(node, prio):
    if node.data in event_finder:
        remove_event(node.data)

    entry = [prio, node.data]
    heappush(pq, entry)
    # Here storing the node object as well
    event_finder[node.data] = (entry, node)

def remove_event(data):
    if data not in event_finder:
        return

    entry, node = event_finder[data]
    event_finder.pop(data)

    last_entry = pq[-1]
    entry[0] = last_entry[0]
    entry[1] = last_entry[1]
    pq.pop(-1)
    heapify(pq)

def pop_event():
    prio, data = heappop(pq)
    entry, node = event_finder.pop(data)

    return([node, prio])

class Vertex:
    def __init__(self, data):
        self.data = data
        self.nbrs = []

    def add_edge(self, n, wt):
        self.nbrs.append([n, wt])

def cheapest_path(s, e):
    exhausted = set()

    add_event(s, 0)
    distances = {s:0}
    back_refs = {s:None}

    while pq:
        v, dist = pop_event()
        #print(v.data, dist)

        for n, wt in v.nbrs:
            if n in exhausted:
                continue

            new_dist = wt + dist
            cur_dist = distances[n] if n in distances else float('inf')
            updated_dist = min(new_dist, cur_dist)
            distances[n] = updated_dist
            add_event(n, updated_dist)

            if updated_dist != cur_dist:
                back_refs[n] = v

    path = []
    if e in back_refs:
        curr = e
        while curr:
            path.append(curr.data)
            curr = back_refs[curr]

    return path[::-1]

v0 = Vertex(0)
v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)

v0.add_edge(v1, 3)
v0.add_edge(v2, 4)
v1.add_edge(v3, 1)
v2.add_edge(v3, 1)

print(cheapest_path(v0, v3))

