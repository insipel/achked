#!/usr/python3 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mirror(node: TreeNode) -> TreeNode:
    if not node:
        return None

    mirror(node.left)
    mirror(node.right)
    node.left, node.right = node.right, node.left

    return node