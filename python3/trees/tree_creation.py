#!/usr/bin/env python3

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node, data):

    parent = None
    while node:
        parent = node
        #print("node: ", node.data)
        if node.data == data:
            return
        elif node.data < data:
            #print("go right: ")
            node = node.right
        else:
            #print("go left: ")
            node = node.left

    new_node = Node(data)
    if (parent.data > data):
        #print("Attaching ", data, " to the left:", parent.data)
        parent.left = new_node
    else:
        #print("Attaching ", data, " to the right:", parent.data)
        parent.right = new_node

def create_tree(l):

    root = Node(l[0])
    for data in l[1:]:
        insert(root, data)

    return root

def print_tree(root):

    if not root:
        print(".")
        return
    print_tree(root.left)
    print(root.data)
    print_tree(root.right)

def print_level_tree(root):
    q = []

    node = root
    level = 0
    prev_level = -1
    q.append([node, level])

    while q:
        node, level = q.pop(0)
        if prev_level != level:
            print()
            prev_level = level
        if node:
            print(" %02d" % (node.data), end=' ')
        else:
            print(' .', end = ' ')

        #if node.left:
        if node:
            q.append([node.left, level+1])
        #if node.right:
        if node:
            q.append([node.right, level+1])

    print()

def main():
    print("Creating a tree")
    l = [6, 3, 10, 2, 5, 7, 12, 1, 4, 8, 11, 14]
    print(l)
    root = create_tree(l)
    #print_tree(root)
    print_level_tree(root)

if __name__ == '__main__':
    main()
