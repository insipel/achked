#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def serialize(node, output):
    if not node:
        output.append(-1)
        return

    output.append(node.data)

    serialize(node.left, output)
    serialize(node.right, output)

def deserialize(output, idx):
    i = idx[0]
    if not output or output[i] == -1:
        return None

    node = Node(output[i])
    idx[0] += 1
    node.left = deserialize(output, idx)

    idx[0] += 1
    node.right = deserialize(output, idx)

    return node

def print_tree(node):
    if not node:
        return

    print(node.data, end = ", ")
    print_tree(node.left)
    print_tree(node.right)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n4.left = n1
n1.right = n2
n2.right = n3
n4.right = n7
n7.left = n6
n6.left = n5
print_tree(n4)
print()

output = []
serialize(n4, output)
print(output)

idx = [0]
node1 = deserialize(output, idx)
print_tree(node1)
print()

