#!/usr/bin/env python3

class Node:

    def __init__(self, data):
        self.data = data
        self.rank = 1
        self.left = None
        self.right = None

def insert_rank_iter(root, data):

    parent = None
    while root:
        parent = root

        if root.data == data:
            print("Found a duplicate insert")
            break
        elif root.data > data:
            root.rank += 1
            root = root.left
        else: #root.data < data
            root.rank += 1
            root = root.right

    if parent.data > data:
        parent.left = Node(data)
    elif parent.data < data:
        parent.right = Node(data)

def print_rank_tree(root):

    if not root:
        return

    print_rank_tree(root.left)
    print("[", root.data, root.rank, "]", end = ' ')
    print_rank_tree(root.right)

def create_rank_tree(l):
    root = Node(l[0])
    for data in l[1:]:
        insert_rank_iter(root, data)

    return root

def find_kth_rank(root, k):

    while root:
        print("Data: ", root.data, ", rank:", root.rank)

        cur_rank = 1
        if root.left:
            cur_rank = root.left.rank + 1

        if cur_rank  == k:
            return root.data
        elif cur_rank < k:
            root = root.right
            k = k - cur_rank
        else:
            root = root.left

    return -1

def main():
    l = [10, 3, 4, 12, 19, 11, 8]
    root = create_rank_tree(l)
    print_rank_tree(root)
    print()
    print(find_kth_rank(root, 5))

if __name__ == '__main__':
    main()

