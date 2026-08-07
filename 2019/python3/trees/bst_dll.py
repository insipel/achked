#!/usr/bin/env python3

from tree_creation import create_tree, print_level_tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bst_to_dll(root):
    if not root:
        return None
    
    head = [None]  # Using a list to hold mutable reference across recursive calls
    prev = [None]
    
    def convert(node):
        if not node:
            return
        
        # 1. Recursively convert the left subtree
        convert(node.left)
        
        # 2. Process the current node
        if prev[0] is None:
            # This is the first node visited (the minimum value / head of DLL)
            head[0] = node
        else:
            # Link current node with the previous node
            node.left = prev[0]     # DLL 'prev' pointer
            prev[0].right = node    # DLL 'next' pointer
            
        # Update prev to the current node before moving to the right subtree
        prev[0] = node
        
        # 3. Recursively convert the right subtree
        convert(node.right)
        
    convert(root)
    return head[0]

def bst_dll_old(node, prev_node, header):
    # This algorithm is about finding inorder successor and predecessor
    # and link the nodes.
    if not node:
        return

    bst_dll_old(node.left, prev_node, header)

    if prev_node[0]:
        prev_node[0].right = node
        node.left = prev_node[0]
    
    if not header[0]:
        # sets the DLL head for the first time.
        header[0] = node

    prev_node[0] = node
    bst_dll_old(node.right, prev_node, header)

def is_bst(node, low, high):
    if not node:
        return True

    if not is_bst(node.left, low, node.data):
        return False

    if node.data < low or node.data > high:
        return False
    
    if not is_bst(node.right, node.data, high):
        return False

    return True

def main():
    # l = [12, 6, 19, 4, 8, 9,  14, 13, 1, 8, 16, 22, 28]
    l = [12, 6, 19, 4, 8, 9,  14, 13, 1, 16, 22, 28]
    #l = [2, 1, 3, 4]
    print(f"arr: {l}")
    root = create_tree(l)
    #print_tree(root)
    print_level_tree(root)
    print(f"Tree is BST?: {is_bst(root, float('-inf'), float('inf'))}")
    prev_node = [None]
    header = [None]
    # bst_dll_old(root, prev_node, header)
    prev_node, header = [None], [None]
    header[0] = bst_to_dll(root)

    node = header[0]
    while node:
        print(node.data,", ", end=' ')
        node = node.right
    print()

if __name__ == '__main__':
    main()

