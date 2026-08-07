class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def clone_tree(root):
    # Base case: if the tree or subtree is empty, return None
    if not root:
        return None
    
    # 1. Create a new clone node with the same data
    cloned_node = Node(root.data)
    
    # 2. Recursively clone the left and right subtrees and attach them
    cloned_node.left = clone_tree(root.left)
    cloned_node.right = clone_tree(root.right)
    
    # 3. Return the newly created root of the cloned subtree
    return cloned_node