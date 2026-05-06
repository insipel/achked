#!/usr/bin/env python3

from tree_creation import create_tree, print_tree, print_level_tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = left
        self.right = right

def preorder_iter(node):
    s = []

    print("Preoder list: ", end = '')
    while s or node:
        if node:
            s.append(node)
            print(node.data, end = ' ')
            node = node.left
        else:
            node = s.pop(-1)
            node = node.right
    print()

def inorder_iter(node):
    s = []

    print("Inorder list: ", end = '')
    while node or s:
        if node:
            s.append(node)
            node = node.left
        else:
            node = s.pop(-1)
            print(node.data, end = ' ')
            node = node.right
    print()

def postorder_iter(node):
    s = []

    print("Postorder list: ", end = '')
    while node or s:
        if node:
            if node.right:
                s.append(node.right)
            s.append(node)
            node = node.left
        else:
            node = s.pop(-1)
            #if not node:
            #    continue

            if not node.right:
                print(node.data, end = ' ')
                node = None
            else:
                if s: # this check is needed for the root when there
                      # won't be any more element in the stack
                    nxt_node = s[-1]
                else:
                    nxt_node = None
                if node.right == nxt_node:
                    nxt_node = s.pop(-1)
                    s.append(node)
                    node = nxt_node
                else:
                    print(node.data, end = ' ')
                    node = None
    print()

def main():
    l = [23, 15, 6, 21, 20, 18, 19, 43, 32, 36, 39, 44, 45]
    root = create_tree(l)
    print_tree(root)
    print_level_tree(root)
    preorder_iter(root)
    inorder_iter(root)
    postorder_iter(root)

if __name__ == '__main__':
    main()

