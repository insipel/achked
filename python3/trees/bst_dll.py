#!/usr/bin/env python3

from tree_creation import create_tree, print_level_tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bst_dll(root, prev_node, header):
    if not root:
        return

    bst_dll(root.left, prev_node, header)

    if prev_node[0]:
        prev_node[0].right = root
        root.left = prev_node[0]
    else:
        header[0] = root

    prev_node[0] = root
    bst_dll(root.right, prev_node, header)

def main():
    l = [12, 6, 19, 4, 8, 14, 13, 1, 8, 16, 22, 28]
    #l = [2, 1, 3, 4]
    print(l)
    root = create_tree(l)
    #print_tree(root)
    print_level_tree(root)
    prev_node = [None]
    header = [None]
    bst_dll(root, prev_node, header)

    node = header[0]
    while node:
        print(node.data,", ", end=' ')
        node = node.right

if __name__ == '__main__':
    main()

