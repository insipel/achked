"""
Problem Statement:
------------------
Given two BSTs (Binary Search Trees), one with N1 nodes and another with N2 nodes.
Your task is to merge them such that:
   - Resultant tree is height-balanced.
   - Resultant tree is a valid BST.
   - Resultant tree contains all values from given BST-1.
   - Resultant tree contains all values from given BST-2.
   - Size of the resultant tree is N1 + N2.
   - For any value, number of occurrences in the resultant tree = 
     occurrences in BST-1 + occurrences in BST-2.
"""

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def merge_bsts(root1: TreeNode, root2: TreeNode) -> TreeNode:
    """
    Merges two BSTs into a single height-balanced BST in O(N1 + N2) time.
    """
    # Step 1: Extract sorted elements via in-order traversal
    list1 = []
    _inorder_traversal(root1, list1)
    
    list2 = []
    _inorder_traversal(root2, list2)
    
    # Step 2: Merge the two sorted lists
    merged_list = _merge_sorted_lists(list1, list2)
    
    # Step 3: Build a height-balanced BST from the merged sorted list
    return _sorted_array_to_bst(merged_list, 0, len(merged_list) - 1)


def _inorder_traversal(root: TreeNode, result: list):
    """Helper function to perform in-order traversal (Left -> Node -> Right)."""
    if not root:
        return
    _inorder_traversal(root.left, result)
    result.append(root.val)
    _inorder_traversal(root.right, result)


def _merge_sorted_lists(list1: list, list2: list) -> list:
    """Helper function to merge two sorted lists into one sorted list (like Merge Sort)."""
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    return merged + list1[i:] + list2[j:]


def _sorted_array_to_bst(arr: list, start: int, end: int) -> TreeNode:
    """Helper function to construct a height-balanced BST from a sorted array."""
    if start > end:
        return None
    
    mid = (start + end) // 2
    root = TreeNode(arr[mid])
    root.left = _sorted_array_to_bst(arr, start, mid - 1)
    root.right = _sorted_array_to_bst(arr, mid + 1, end)
    
    return root


# ==========================================
# Unit Tests
# ==========================================
import unittest

def build_tree_from_list(lst):
    """Helper to build a BST from a list by successive insertions."""
    if not lst:
        return None
    root = None
    for val in lst:
        root = insert_into_bst(root, val)
    return root

def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val <= root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def get_tree_height(root):
    """Calculates height of the tree (edges in longest path)."""
    if not root:
        return -1
    return max(get_tree_height(root.left), get_tree_height(root.right)) + 1

def count_nodes(root):
    """Counts total nodes in a tree."""
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

class TestMergeBSTs(unittest.TestCase):
    
    def test_merge_standard_bsts(self):
        # BST-1: [3, 1, 5] -> Inorder: [1, 3, 5]
        bst1 = build_tree_from_list([3, 1, 5])
        # BST-2: [4, 2, 6] -> Inorder: [2, 4, 6]
        bst2 = build_tree_from_list([4, 2, 6])
        
        merged_root = merge_bsts(bst1, bst2)
        
        # Check size (N1 + N2 = 3 + 3 = 6)
        self.assertEqual(count_nodes(merged_root), 6)
        
        # Check in-order sorted order property of BST
        inorder = []
        _inorder_traversal(merged_root, inorder)
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6])
        
        # Check height-balanced property (height for 6 nodes should be <= 2)
        height = get_tree_height(merged_root)
        self.assertLessEqual(height, 2)

    def test_merge_with_duplicates(self):
        # BST-1 with duplicate values
        bst1 = build_tree_from_list([5, 3, 5])
        # BST-2 with duplicate values
        bst2 = build_tree_from_list([5, 2])
        
        merged_root = merge_bsts(bst1, bst2)
        
        # Total nodes = 3 + 2 = 5
        self.assertEqual(count_nodes(merged_root), 5)
        
        inorder = []
        _inorder_traversal(merged_root, inorder)
        # Check that all occurrences are preserved and sorted
        self.assertEqual(inorder, [2, 3, 5, 5, 5])

    def test_merge_one_empty_tree(self):
        bst1 = build_tree_from_list([10, 5, 15])
        bst2 = None
        
        merged_root = merge_bsts(bst1, bst2)
        
        self.assertEqual(count_nodes(merged_root), 3)
        inorder = []
        _inorder_traversal(merged_root, inorder)
        self.assertEqual(inorder, [5, 10, 15])

    def test_merge_both_empty_trees(self):
        merged_root = merge_bsts(None, None)
        self.assertIsNone(merged_root)


if __name__ == '__main__':
    unittest.main()