#!/usr/bin/env python3

from tree_creation import print_level_tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_walk(root, in_list, n1, n2):
    if n1 in in_list and n2 in in_list:
        return True

    if not root:
        return False

    if (inorder_walk(root.left, in_list, n1, n2)):
        return True

    in_list.append(root.data)

    if (inorder_walk(root.right, in_list, n1, n2)):
        return True

    return False

def postorder_walk(root, pmap, n1, n2, l):
    if not root:
        return False

    #if n1 in pmap and n2 in pmap:
    #    return True

    if (postorder_walk(root.left, pmap, n1, n2, l)):
        return True

    if (postorder_walk(root.right, pmap, n1, n2, l)):
        return True

    l[0] += 1
    pmap[root.data] = l[0]

# This method works with inorder and postorder strings
def find_lca1(root, n1, n2):
    in_list = []
    print(inorder_walk(root, in_list, n1, n2))
    #if the above function returns False, then return error since both
    #n2 and n2 are not found in the tree.
    print(in_list)

    post_map = {}
    l = [0]
    postorder_walk(root, post_map, n1, n2, l)
    print(post_map)

    max_index = -1
    lca_node = -1

    for data in in_list:
        pmap_data = post_map[data]
        if pmap_data > max_index:
            max_index = pmap_data
            lca_node = data

    return lca_node

# This method works recursively without additional space req
def find_lca2(root, n1, n2):
    if not root:
        return None

    if n1 == root.data or n2 == root.data:
        return root

    left_node = find_lca2(root.left, n1, n2)
    right_node = find_lca2(root.right, n1, n2)

    if not left_node and not right_node:
        return None

    if left_node and right_node:
        return root

    return left_node if left_node else right_node

def find_lca2_error_chk(root, n1, n2, found_list):
    if not root:
        return None

    if root.data == n1:
        found_list[0] = True
        return root
    if root.data == n2:
        found_list[1] = True
        return root

    left_node = find_lca2_error_chk(root.left, n1, n2, found_list)
    right_node = find_lca2_error_chk(root.right, n1, n2, found_list)

    if not left_node and not right_node:
        return None
    if left_node and right_node:
        return root
    return left_node if left_node else right_node

def main():

    root = Node(15)
    left = root.left = Node(10)
    right = root.right = Node(19)
    left.left = Node(5)
    left.right = Node(12)
    left.right.right = Node(13)
    left.right.left = Node(6)

    #root = Node(3)
    #root.left = Node(5)
    #root.right = Node(4)
    #root.right.right = Node(2)

    print_level_tree(root)
    n1 = 6
    n2 = 20

    #print("LCA of ", n1, " and ", n2, " is ", find_lca1(root, n1, n2))

    #lca = find_lca2(root, n1, n2)
    #print("LCA of ", n1, " and ", n2, " is ", lca.data)

    found_list = [False] * 2
    lca = find_lca2_error_chk(root, n1, n2, found_list)
    if not found_list[0] or not found_list[1]:
        print("Node ", n2 if found_list[0] else n1, " doesn't exist")
    else:
        print("LCA of ", n1, " and ", n2, " is ", lca.data)

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

