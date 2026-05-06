#!/usr/bin/env python3

from tree_creation import print_level_tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_paths(root, s):
    if not root:
        return

    s.append(root.data)
    print_paths(root.left, s)
    print_paths(root.right, s)

    if not root.left and not root.right:
        print(s)
    s.pop(-1)

def main():
    root = Node(2)
    left = root.left = Node(3)
    right = root.right = Node(4)

    left.right = Node(-9)
    left.right.left = Node(10)

    right.left = Node(34)
    right.left.left = Node(16)
    right.left.right = Node(22)
    right.left.left.right = Node(-17)

    print_level_tree(root)

    s = []
    print_paths(root, s)

if __name__ == '__main__':
    main()

