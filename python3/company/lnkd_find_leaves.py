#!/usr/bin/env python3

def findLeaves(self, root):
    out = []

    def dfs(node):
        if not node:
            return -1
        i = 1 + max(dfs(node.left), dfs(node.right))
        if i == len(out):
            out.append([])
        out[i].append(node.val)

        node.left = None
        node.right = None

        return i

    dfs(root)
    return out

'''
Find Leaves of Binary Tree
Medium

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

 

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]

'''
