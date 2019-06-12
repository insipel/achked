#!/usr/bin/env python3

from tree_creation import create_tree, print_level_tree

def insert_left(root, st):
    while root:
        st.append(root)
        root = root.left

def dfs(root):
    st = []
    insert_left(root, st)
    print()
    while st:
        node = st.pop(-1)
        print(node.data, end=' ')
        insert_left(node.right, st)
    print()

def main():
    l = [23, 14, 26, 19, 9, 33, 31, 28, 29, 6, 2]
    root = create_tree(l)
    print_level_tree(root)
    dfs(root)

if __name__ == '__main__':
    main()
