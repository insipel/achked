#!/usr/bin/env python3

#  a tree is unival in x if and only if every node within the tree has the value x
# is_unival(treeNode)
# unival_subtreecount(treeNode)
#   1
# 1   1 -> 3

#    1
#  1   1
#     2  -> 2

#    1
#  2   3
# 2 2 3 3 -> 6

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def unival_count(node):
    if not node:
        return True, -1, 0
    
    lunival, lval, lsz = unival_count(node.left)
    runival, rval, rsz = unival_count(node.right)
        
    if lunival and runival:
        
        if not node.left and not node.right:
            return True, node.data, 1
        
        if node.left and node.right and node.data == lval and node.data == rval:
            cur_sz = lsz + rsz + 1
            return True, node.data, cur_sz
        
        if node.left and not node.right and node.data == lval:
            return True, node.data, lsz + 1
        
        if node.right and not node.left and node.data == rval:
            return True, node.data, rsz + 1
        
        else:
            return False, -1, lsz+rsz
        #
        #cur_sz = lsz + rsz
                  
    
    #lif lunival:
    #   return False, -1, lsz+rsz
    else:
        return False, -1, lsz+rsz
    

n1 = Node(1)

n2 = Node(2)
n3 = Node(2)
n4 = Node(2)

n5 = Node(3)
n6 = Node(3)
n7 = Node(3)
n1.left = n2
n1.right = n5

n2.left = n3
n2.right = n4

n5.left = n6
n5.right = n7

#print(unival_count(n1))
        
        
def is_unival(node, x):
    if not node:
        return True, 0
    
    if node.data != x:
        return False, 
    
    if not is_unival(node.left, x):
        return False
    
    if not is_unival(node.right, x):
        return False
    
    return True

n1 = Node(1)
n2 = Node(1)
n3 = Node(3)
n4 = Node(1)
n2.left = n1
n1.right = n3
n2.right = n4
#print(is_unival(n2, 1))

n1 = Node(1)
n2 = Node(1)
n3 = Node(1)
n4 = Node(1)
n2.left = n1
n1.right = n3
n2.right = n4
#print(is_unival(n2, 1))

