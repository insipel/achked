#!/usr/bin/env python3

class Vertex:
    def __init__(self, label):
        self.label = label
        self.nbrs = []

    def add_edge(self, node):
        self.nbrs.append(node)

def explore(node, seen, comp):
    if node.label in seen:
        return

    seen.add(node.label)
    comp.append(node.label)

    for nbr in node.nbrs:
        explore(nbr, seen, comp)

    return

def dfs(node_list):

    seen = set()

    for node in node_list:
        if node.label not in seen:
            comp = []
            explore(node, seen, comp)
            print(comp)

    return

def test1():
    n1 = Vertex(1)
    n2 = Vertex(2)
    n3 = Vertex(3)
    n1.add_edge(n2)
    n2.add_edge(n3)
    l = []
    l.append(n1)
    l.append(n2)
    l.append(n3)
    return l

def test2():
    n1 = Vertex(1)
    n2 = Vertex(2)
    n3 = Vertex(3)
    n4 = Vertex(4)
    n5 = Vertex(5)
    n6 = Vertex(6)
    n7 = Vertex(7)
    n1.add_edge(n2)
    #n1.add_edge(n3)
    n2.add_edge(n4)
    #n3.add_edge(n4)
    n4.add_edge(n3)

    n4.add_edge(n5)
    n4.add_edge(n6)
    n6.add_edge(n4)
    n5.add_edge(n7)
    n6.add_edge(n7)

    l = []
    l.append(n1)
    l.append(n2)
    l.append(n3)
    l.append(n4)
    l.append(n5)
    l.append(n6)
    l.append(n7)
    return l

def main():
    l = test1()
    dfs(l)
    l = test2()
    dfs(l)


if __name__ == '__main__':
    main()

