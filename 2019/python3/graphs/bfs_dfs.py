#!/usr/bin/env python3

from collections import deque
from random import randint

class Vertex:
    
    def __init__(self, data):
        self.data = data
        self.neighbors = []

    def add_edge(self, a):
        self.neighbors.append(a)

def dfs(node):
    seen = set()
    print("in dfs")
    
    def _dfs(node):
        seen.add(node.data)
        for nxt in node.neighbors:
            if nxt.data not in seen:
                _dfs(nxt)
        print(node.data)

    _dfs(node)

def bfs_using_vars(node):
    seen = set()
    q = deque()

    q.append(node)
    num_prelevel = 1
    cur_level = 0
    s = str(node.data)

    while q:
        node = q.popleft()
        num_prelevel -= 1
        print("after pop:", num_prelevel)

        if not num_prelevel:
            print(s)
            s = ''
            cur_level += 1

        seen.add(node.data)
        for nxt in node.neighbors:
            if nxt.data not in seen:
                q.append(nxt)
                num_prelevel += 1
                s += str(nxt.data) + ','
                print("num_prelevel", num_prelevel, "string:", s)

def bfs(node):
    seen = set()
    q = deque()
    l = []

    prev_level = level = 0
    q.append([node, level])
    s = ''

    while q:
        node, level = q.popleft()

        seen.add(node.data)

        if (level != prev_level):
            print(s)
            s = ''
            prev_level = level

        s += str(node.data) + ","

        for nxt in node.neighbors:
            if nxt.data not in seen:
                q.append([nxt, level + 1])
    print(s)

node1 = Vertex(1)
node2 = Vertex(2)
node3 = Vertex(3)
node4 = Vertex(4)
node5 = Vertex(5)
node6 = Vertex(6)
node1.add_edge(node2)
node2.add_edge(node4)
node2.add_edge(node5)
node4.add_edge(node3)
node5.add_edge(node4)
node5.add_edge(node6)
node6.add_edge(node1)
node6.add_edge(node2)
bfs(node1)


#if __name__ == '__main__' :
#    pass
