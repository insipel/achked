#!/usr/bin/env python3

from build_graph import *

def bfs(node_list):
    q = []
    comp = []
    seen = set()
    q.append(node_list[0])

    while q:
        node = q.pop(0)

        if node.label not in seen:
            comp.append(node.label)
            seen.add(node.label)

            for nbr in node.nbrs:
                q.append(nbr)

    print(comp)

def main():
    l = test2()
    bfs(l)
    dfs(l)

if __name__ == '__main__':
    main()

