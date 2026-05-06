#!/usr/bin/env python3

from tree_creation import create_tree, print_level_tree, print_tree

# Augment the node datastructure to include the number of nodes in its
# left subtree. if K = node.left_elems + 1, then node is the answer
# else if K < node.left_elemns, search in left subtree, else search in
# right subtree for (K - node.left_elems - 1).

def pushleft(node, s):
    while node:
        s.append(node)
        node = node.left


# Iterative kth smallest element finder algorithm
def find_kth_smallest_iter(root, l):
    s = []
    pushleft(root, s)

    while s:
        node = s.pop(-1)
        l[0] -= 1
        if l[0] == 0:
            l[1] = node.data
            return

        node = node.right
        pushleft(node, s)

    l[0] = -1
    return
        

# Recursive kth smallest element finder algorithm
def find_kth_smallest(root, l):
    print("k:", l[0], "root.data:", root.data if root else -1)
    #if l[0] <= 0 or not root:
    if l[0] <= 0 or not root:
        return

    if root.left:
        find_kth_smallest(root.left, l)

    if l[0] > 0:
        l[0] -= 1
        print("l[0]: ", l[0], "root.data:", root.data if root else -1)
        if (l[0] == 0):
            l[1] = root.data
            return

    if root.right:
        find_kth_smallest(root.right, l)

    return

def find_kth_largest_iter(root, l):
    #print("k:", l[0], "root.data:", root.data if root else -1)
    #if l[0] <= 0 or not root:
    k = l[0]
    if not l[0] or not root:
        return

    if root.right:
        find_kth_larget_rec(root.right, l)

    if l[0] > 0:
        l[0] -= 1
        print("l[0]: ", l[0], "root.data:", root.data if root else -1)
        if (l[0] == 0):
            l[1] = root.data
            return

    if root.left:
        find_kth_larget_rec(root.left, l)

    return

def find_kth_largest_rec(root, l):
    #print("k:", l[0], "root.data:", root.data if root else -1)
    #if l[0] <= 0 or not root:
    if not l[0] or not root:
        return

    if root.right:
        find_kth_larget_rec(root.right, l)

    if l[0] > 0:
        l[0] -= 1
        print("l[0]: ", l[0], "root.data:", root.data if root else -1)
        if (l[0] == 0):
            l[1] = root.data
            return

    if root.left:
        find_kth_larget_rec(root.left, l)

    return

def main():
    print("finding kth smallest element in a tree")
    l = [12, 6, 19, 4, 8, 14, 13, 1, 8, 16, 22, 28]
    #l = [2, 1, 3, 4]
    print(l)
    root = create_tree(l)
    #print_tree(root)
    print_level_tree(root)
    k = 5
    list_k = [k, -1]
    #list_k.append(k)
    #find_kth_smallest(root, list_k)
    #find_kth_smallest_iter(root, list_k)
    #find_kth_largest_rec(root, list_k)
    find_kth_largest_iter(root, list_k)
    if list_k[0] == -1:
        print(k, "th element not present!!")
    else:
        print(k, "th element is:" , list_k[1])

if __name__ == '__main__':
    main()

