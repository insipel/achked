#!/usr/bin/env python3

left = 1
right = 2

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def stretch(root, k):

    if k <= 1:
        return root

    return _stretch(root, k, left)

def _stretch(root, k, direction):
    if not root:
        return None

    #
    # go to a node, calculate new node value
    # orig_node = root
    # first_node = None
    # in a loop of k - 1, get dir
    #   new_node = Node(new_val)
    #   if not first_node:
    #      first_node = new_node
    #   if dir == 1:
    #       node.left = new_node
    #       node = new_node
    #   else: right child additions
    #
    #   if dir == left:
    #      node.left = orig_node
    #      orig_node.data = new_val
    #      orig_node.left = _stretch(orig_node.left, k)
    #   else:
    #      node.right = stretch(orig_node.right, k)
    #
    #   return first_node
    orig_node = root
    new_val = int(root.data/k)
    first_node = Node(new_val)
    prev_node = first_node

    for i in range(k-2):
        new_node = Node(new_val)

        if direction == left:
            prev_node.left = new_node
        else:
            prev_node.right = new_node
        prev_node = new_node

    orig_node.data = new_val
    if direction == left:
        prev_node.left = orig_node
    else:
        prev_node.right = orig_node

    orig_node.right = _stretch(orig_node.right, k, right)
    orig_node.left = _stretch(orig_node.left, k, left)

    return first_node


def print_tree(node):
    if not node:
        return None

    print(node.data, end = ", ")
    print_tree(node.left)
    print_tree(node.right)


n1 = Node(12)
n2 = Node(81)
n3 = Node(56)
n4 = Node(34)
n5 = Node(19)
n6 = Node(6)

n1.left = n2
n1.right = n4
n2.right = n3
n4.left = n5
n4.right = n6

#print_tree(stretch(n1, 0))
#print_tree(stretch(n1, 1))
#print_tree(stretch(n1, 2))
#print_tree(stretch(n1, 3))
print_tree(stretch(n1, 4))

