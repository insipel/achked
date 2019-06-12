#!/usr/bin/env python3

from tree_creation import *

def tree_height(root):
    if not root:
        return -1

    lh = tree_height(root.left)
    rh = tree_height(root.right)
    h = max(lh, rh)
    return h+1

def main():
    l = [10, 6, 9, 8, 11, 13, 12, 7]
    root = create_tree(l)
    print_level_tree(root)
    print("Tree height is:", tree_height(root))

if __name__ == '__main__':
    main()

