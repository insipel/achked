#!/usr/bin/env python3

from tree_creation import create_tree, print_level_tree, print_tree

'''
def pushleft(node, s):
    while node:
        s.append(node)
        node = node.left


def find_kth_largest_iter(root, l):
    return

def find_kth_largest_rec(root, l):
    #print("k:", l[0], "root.data:", root.data if root else -1)
    #if l[0] <= 0 or not root:
    if not l[0] or not root:
        return

    if root.right:
        find_kth_largest_rec(root.right, l)

    if l[0] > 0:
        l[0] -= 1
        print("l[0]: ", l[0], "root.data:", root.data if root else -1)
        if (l[0] == 0):
            l[1] = root.data
            return

    if root.left:
        find_kth_largest_rec(root.left, l)

    return
'''

def main():
    print("-" * 10)
    print("finding kth largest element in a tree")
    l = [12, 6, 19, 4, 8, 14, 13, 1, 8, 16, 22, 28]
    #l = [2, 1, 3, 4]
    print(l)
    root = create_tree(l)
    #print_tree(root)
    # print_level_tree(root)
    k = 5
    list_k = [k, -1]
    #list_k.append(k)
    #find_kth_largest_rec(root, list_k)
    # find_kth_largest_iter(root, list_k)
    if list_k[0] == -1:
        print(k, "th element not present!!")
    else:
        print(k, "th element is:" , list_k[1])


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_largest_iterative(root: TreeNode, k: int) -> int:
    """Finds the k-th largest element using an iterative reverse in-order traversal.
    
    Time Complexity: O(H + k)
    Space Complexity: O(H) where H is the height of the tree.
    """
    stack = []
    curr = root
    count = 0

    while curr or stack:
        # 1. Push all right children to stack (go to the largest elements)
        while curr:
            stack.append(curr)
            curr = curr.right

        # 2. Process current node (largest unvisited)
        curr = stack.pop()
        count += 1

        if count == k:
            return curr.val

        # 3. Move to left subtree
        curr = curr.left

    return -1  # If k is larger than the number of nodes in the BST

def kth_largest_recursive(root: TreeNode, k: int) -> int:
    """Finds the k-th largest element using recursive reverse in-order traversal with early stopping.
    
    Time Complexity: O(H + k)
    Space Complexity: O(H) call stack space.
    """
    # state[0] tracks remaining count (k)
    # state[1] holds the result value
    state = [k, None]

    def reverse_inorder(node):
        if not node or state[0] <= 0:
            return

        # Traverse Right Subtree (larger elements)
        reverse_inorder(node.right)

        # Process Current Node
        if state[0] > 0:
            state[0] -= 1
            if state[0] == 0:
                state[1] = node.val
                return  # Early exit from current stack frame

        # Traverse Left Subtree (smaller elements)
        if state[0] > 0:
            reverse_inorder(node.left)

    reverse_inorder(root)
    return state[1]


# Helper to insert nodes to build a valid BST
def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

if __name__ == "__main__":
    # Construct BST:
    #        50
    #      /    \
    #    30      70
    #   /  \    /  \
    #  20  40  60  80
    
    values = [50, 30, 70, 20, 40, 60, 80]
    root = None
    for v in values:
        root = insert(root, v)

    # Sorted order descending: [80, 70, 60, 50, 40, 30, 20]
    
    k = 3
    print(f"{k}-rd Largest (Iterative):", kth_largest_iterative(root, k))  # Output: 60
    print(f"{k}-rd Largest (Recursive):", kth_largest_recursive(root, k))  # Output: 60

    main()

