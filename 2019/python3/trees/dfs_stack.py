#!/usr/bin/env python3

from tree_creation import create_tree, print_level_tree

def dfs_manual(root):
    s = []
    node = root
    while node:
        s.append(node)
        node = node.left

    while s:
        node = s.pop(-1)
        print(node.data, end=' ')
        node = node.right
        while node:
            s.append(node)
            node = node.left
    print()

def main():
    print("Tree DFS traversal with manual stack")
    l = [12, 5, 6, 3, 1, 15, 19, 21, 13, 14, 23]
    print(l)
    root = create_tree(l)
    print_level_tree(root)
    dfs_manual(root)

if __name__ == '__main__':
    main()

