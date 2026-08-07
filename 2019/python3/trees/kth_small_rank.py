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

def find_kth_rank_iter(root, k):
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

class AugmentedTreeNode:
    """
    Binary Search Tree Node augmented with a `size` field.
    `size` stores the total number of nodes in the subtree rooted at this node.
    """
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1  # A new node starts with a subtree size of 1 (itself)


def get_size(node: AugmentedTreeNode) -> int:
    """Helper to safely retrieve node size handling None references."""
    return node.size if node else 0

def insert_rec(root: AugmentedTreeNode, val: int) -> AugmentedTreeNode:
    """
    Inserts a value into the BST and updates the `size` property 
    along the insertion path in O(H) time.
    """
    if not root:
        return AugmentedTreeNode(val)

    if val < root.val:
        root.left = insert_rec(root.left, val)
    else:
        root.right = insert_rec(root.right, val)

    # Recalculate size as the recursion unwinds back up to the root
    root.size = 1 + get_size(root.left) + get_size(root.right)
    return root


def kth_smallest_recursive(root: AugmentedTreeNode, k: int) -> int:
    """
    Finds the k-th smallest element in O(H) time by making O(1) size checks.
    (Note: k is 1-indexed)
    """
    if not root or k <= 0 or k > get_size(root):
        return None  # Handle out-of-bounds k or empty tree

    left_size = get_size(root.left)

    # Case 1: The current node is the k-th smallest
    if k == left_size + 1:
        return root.val

    # Case 2: The k-th smallest element is in the left subtree
    elif k <= left_size:
        return kth_smallest_recursive(root.left, k)

    # Case 3: The k-th smallest element is in the right subtree
    else:
        # Subtract left subtree size + current node from k
        return kth_smallest_recursive(root.right, k - left_size - 1)

def main():
    print("printing kth_smallest_iter result")
    l = [10, 3, 4, 12, 19, 11, 8]
    root = create_rank_tree(l)
    print_rank_tree(root)
    print()
    k = 5
    print(f"kth:{k} rank element {find_kth_rank_iter(root, k)}")

# =====================================================================
# Example Usage & Test Case
# =====================================================================
if __name__ == "__main__":
    # Constructing a BST with values: [20, 10, 30, 5, 15, 25, 35]
    # Sorted order would be: [5, 10, 15, 20, 25, 30, 35]
    
    values = [20, 10, 30, 5, 15, 25, 35]
    root = None

    print("Inserting values into Augmented BST...")
    for val in values:
        root = insert_rec(root, val)

    print(f"Total Tree Size: {get_size(root)} nodes\n")

    # Retrieve all k-th elements
    total_nodes = get_size(root)
    print("k-th Smallest Query Results:")
    print("-" * 30)
    for k in range(1, total_nodes + 1):
        result = kth_smallest_recursive(root, k)
        print(f"k = {k} -> {result}")

    # Edge Case Tests
    print("\nEdge Cases:")
    print(f"k = 0  (Invalid): {kth_smallest_recursive(root, 0)}")
    print(f"k = 10 (Out of bounds): {kth_smallest_recursive(root, 10)}")

    main()
