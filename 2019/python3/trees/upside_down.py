#!/usr/bin/env python3

from tree_creation import print_level_tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def upside_down(root):
    if not root:
        return root

    l = root.left
    r = root.right
    root.left = root.right = None
    
    while l:
        gl = l.left
        gr = l.right

        l.left = r
        l.right = root

        root = l
        l = gl
        r = gr

    return root

def upside_down_inorder_rec(root, new_node):

    if not root:
        return root

    if root.left:
        upside_down_inorder_rec(root.left, new_node)
        left = root.left
        left.right = root
        left.left = root.right
    else:
        new_node[0] = root

    root.left = root.right = None

def main():
    root = Node(1)
    left = root.left = Node(2)
    root.right = Node(3)

    left.right = Node(5)
    # This thing is so unlike C. Very interesting difference
    left.left = left = Node(4)

    left.right = Node(7)
    left.left = left =  Node(6)

    left.right = Node(9)
    left.left = left = Node(8)

    print_level_tree(root)
    #root = upside_down(root)
    new_root = [None]
    upside_down_inorder_rec(root, new_root)
    print_level_tree(new_root[0])

if __name__ == '__main__':
    main()

