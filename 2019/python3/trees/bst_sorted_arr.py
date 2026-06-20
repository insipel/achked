#!/usr/bin/env python3

from tree_creation import print_level_tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bst_sorted_arr(l, st, end):
    if st > end:
        return None

    mid = st + (end - st)//2
    root = Node(l[mid])
    root.left = bst_sorted_arr(l, st, mid - 1)
    root.right = bst_sorted_arr(l, mid + 1, end)
    return root


def main():
    l = [3, 5, 7, 10, 21, 2, 12, 43, 19, 9]
    l = sorted(l)
    print(l)
    root = bst_sorted_arr(l, 0, len(l) - 1)
    print_level_tree(root)

if __name__ == '__main__':
    main()

