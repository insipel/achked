#!/usr/bin/env python3

def _topo_order(node, order, graph, visited):
    visited.add(node)

    for nbr, wt in graph[node]:
        if nbr not in visited:
            _topo_order(nbr, order, graph, visited)

    order.append(node)

def topo_order(graph):
    order = []
    visited = set()

    for node in graph:
        if node not in visited:
            _topo_order(node, order, graph, visited)

    return order[::-1]

def longest_path(dag_nodes, dag_from, dag_to, dat_wt,
                 from_node, to_node):

    graph = {}
    num_edges = len(dag_from)
    for i in range(num_edges):
        if dag_from[i] not in graph:
            graph[dag_from[i]] = [(dag_to[i], dag_wt[i])]
        else:
            graph[dag_from[i]].append((dag_to[i], dag_wt[i]))

        if dag_to[i] not in graph:
            graph[dag_to[i]] = []

    print(graph)

    order = topo_order(graph)
    print(order)

    back_refs = {from_node: None}
    # longest_path will have the accumulated weight for the nodes
    # along the path, starting with 0 from the start node.
    longest_path = [ -1 for _ in range(dag_nodes + 1)]
    longest_path[from_node] = 0
    print(longest_path)


    for i in range(dag_nodes):
        node = order[i]
        if longest_path[node] >= 0:
            from_wt = longest_path[node]
            #print("node:", node, ", from_wt: ", from_wt)

            if node == to_node:
                break

            for nbr, wt in graph[node]:
                to_wt = longest_path[nbr]
                #print("nbr:", nbr, "to_wt: ", to_wt)
                #print(longest_path)

                if to_wt <= from_wt + wt:
                    longest_path[nbr] = from_wt + wt
                    back_refs[nbr] = node

    # Now prepare the path using back_refs
    path = []
    #if longest_path[to_node] >= 0:
    # either above or below condition should be good
    if to_node in back_refs:
        curr = to_node

        while curr != None:
            path.append(curr)
            curr = back_refs[curr]

    return path[::-1]


dag_from = [1, 1, 4, 5, 5,  2, 2, 3, 11, 11, 6, 6, 6,  7,  8,  9]
dag_to   = [2, 3, 3, 4, 3, 11, 6, 6,  6,  7, 7, 8, 9, 10, 10, 10]
dag_wt   = [2, 2, 3, 4, 3,  1, 1, 4,  3,  1, 2, 4, 3, 10,  1,  9]
dag_nodes = 11

from_node = 2
to_node   = 10
path = longest_path(dag_nodes, dag_from, dag_to, dag_wt, from_node, to_node)
print(path)


