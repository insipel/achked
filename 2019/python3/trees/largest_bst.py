#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def largest(node):
    if not node.left and not node.right:
        return True, node.data, node.data, 1 # sz

    if not node.left:
        lbst, lmin, lmax, lsz = True, node.data, node.data, 0
    else:
        lbst, lmin, lmax, lsz = largest(node.left)

    if not node.right:
        rbst, rmin, rmax, rsz = True, node.data, node.data, 0
    else:
        rbst, rmin, rmax, rsz = largest(node.right)

    if lbst and rbst:
        if node.data >= lmax and node.data <= rmin:
            cur_sz = lsz+rsz+1
            return True, lmin, rmax, cur_sz

    if not rlbst:
        return False, lmin, lmax, lsz

    if rbst:
        return False, rmin, rmax, rsz

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n4.left = n1
n1.right = n2
n2.left = n3
n4.right = n7
n7.left = n6
n6.left = n5
status, min_d, max_d, sz = largest(n4)
print(status, min_d, max_d, sz)

