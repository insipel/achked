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
    find_kth_smallest_iter(root, list_k)
    if list_k[0] == -1:
        print(k, "th element not present!!")
    else:
        print(k, "th element is:" , list_k[1])

# Newer implementation which is simpler and more readable.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest_iterative(root: TreeNode, k: int) -> int:
    stack = []
    pushleft(root, stack)

    while stack:
        # Process the node at the top of the stack
        node = stack.pop()
        k -= 1

        # If we have reached the k-th element, return its value
        if k == 0:
            return node.val

        # Move to the right subtree
        pushleft(node.right, stack)

    return -1  # If k is greater than the total number of nodes

def kth_smallest_recursive(root: TreeNode, k: int) -> int:
    # State tracking variable: [remaining_k, result]
    # We use a list so child stack frames can mutate the values in-place
    state = [k, None]

    def inorder(node):
        # Base case: empty node OR target already found (short-circuit)
        if not node or state[1] is not None:
            return

        # 1. Traverse left subtree
        inorder(node.left)

        # 2. Process current node
        if state[1] is None:
            state[0] -= 1
            if state[0] == 0:
                state[1] = node.val
                return  # Found the kth element!

        # 3. Traverse right subtree (only if target is not yet found)
        if state[1] is None:
            inorder(node.right)

    inorder(root)
    return state[1]

if __name__ == '__main__':
    root = TreeNode(10, TreeNode(7, TreeNode(9, TreeNode(8))), TreeNode(23))
    print(f"kth_smallest new iterative: {kth_smallest_iterative(root, 2)}")
    print(f"kth_smallest new recursive: {kth_smallest_recursive(root, 2)}")
    main()

