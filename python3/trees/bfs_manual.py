#!/usr/bin/env python3

from tree_creation import create_tree, print_level_tree

def bfs_manual(root):
    q = []
    q.append(root)

    while q:
        node = q.pop(0)
        print(node.data, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print()

def main():
    print("Tree BFS traversal with manual queue")
    l = [12, 5, 6, 3, 1, 15, 19, 21, 13, 14, 23]
    print(l)
    root = create_tree(l)
    print_level_tree(root)
    bfs_manual(root)

if __name__ == '__main__':
    main()

