#!/usr/bin/env python3

from build_graph import *

def has_cycle(node_list):
    visited = {}

    for node in node_list:
        if _has_cycle(node, visited):
            return True

    return False

def _has_cycle(node, visited):
    if node in visited:
        if visited[node] == -1:
            return True
        else:
            return False
    visited[node] = -1

    for nbr in node.nbrs:
        if _has_cycle(nbr, visited):
            return True

    visited[node] = 1
    return False

def main():
    l = test2()
    dfs(l)
    print(has_cycle(l))

if __name__ == "__main__":
    main()

