#!/usr/bin/env python3

from tree_creation import print_level_tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_bst_range(root, lo, hi):

    if not root:
        return True

    if not is_bst_range(root.left, lo, root.data):
        return False

    if root.data >= hi or root.data <= lo:
        return False

    if not is_bst_range(root.right, root.data, hi):
        return False

    return True

def is_bst_dnc(root):

    # To cover the null children of leaves
    if not root:
        # What value to return for min and max here??
        return True, -1, -1

    lbst, lmin, lmax = is_bst_dnc(root.left)
    rbst, rmin, rmax = is_bst_dnc(root.right)

    if lbst and rbst:

        lnode = root.left
        rnode = root.right
        cur_data = root.data

        if not lnode and not rnode:
            return True, cur_data, cur_data
        elif lnode and rnode:
            if cur_data > lmax and cur_data < rmin:
                return True, lmin, rmax
        elif lnode and cur_data > lmax:
            return True, lmin, cur_data
        elif rnode and cur_data < rmin:
            return True, cur_data, rmax

    return False, -1, -1


def leet_isValidBST(root):
    prev = None
    return leet_validate(root, prev);

def leet_validate(node, prev):
    if not node:
       return True

    if not leet_validate(node.left, prev):
        return False

    if (prev and prev.data >= node.data):
         return False

    prev = node;
    return leet_validate(node.right, prev);

def main():

    root = Node(15)
    left = root.left = Node(10)
    right = root.right = Node(19)
    left.left = Node(5)
    left.left.right = Node(6)
    left.right = Node(12)
    left.right.right = Node(13)
    #left.right.left = Node(6)
    #root = Node(3)
    #root.left = Node(4)
    #root.right = Node(4)

    print_level_tree(root)
    #if(leet_isValidBST(root)):
    #if(is_bst_range(root, float('-inf'), float('inf'))):
    is_bst, bst_min, bst_max = is_bst_dnc(root)
    if(is_bst):
        print("It's a BST")
    else:
        print("Not a BST")

if __name__ == '__main__':
    main()


'''
bool isValidBST(TreeNode* root) {
    return isValidBST(root, NULL, NULL);
}

bool isValidBST(TreeNode* root, TreeNode* minNode, TreeNode* maxNode) {
    if(!root) return true;
    if(minNode && root->val <= minNode->val || maxNode && root->val >= maxNode->val)
        return false;
    return isValidBST(root->left, minNode, root) && isValidBST(root->right, root, maxNode);
}
'''

'''
public:
    bool isValidBST(TreeNode* root) {
        TreeNode* prev = NULL;
        return validate(root, prev);
    }
    bool validate(TreeNode* node, TreeNode* &prev) {
        if (node == NULL) return true;
        if (!validate(node->left, prev)) return false;
        if (prev != NULL && prev->val >= node->val) return false;
        prev = node;
        return validate(node->right, prev);
    }
};
'''

