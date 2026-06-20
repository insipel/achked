#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        self.random = None

def printlist(head):
    print("List: [", end = '')
    while head:
        print("(", head.data, ",", head.random.data if head.random
                else - 1, ")", end=",")
        head = head.next
    print("]")

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
#n6 = Node(6)
#n7 = Node(7)
#n8 = Node(8)
#n9 = Node(9)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
#n5.next = n6
#n6.next = n7
#n7.next = n8
#n8.next = n9
head = n1
n1.random = n4
n2.random = n3
n3.random = n4
n4.random = n3
n5.random = n2
printlist(head)

def clone_random(node):

    cmap = {}
    prev = None; head = None

    while node:

        data = node.data
        if data not in cmap:
            clone = Node(data+1) # +1 to check if it's a new list
            cmap[data] = clone
        clone = cmap[data]

        if not prev:
            head = clone
        else:
            prev.next = clone

        clone.random = None
        if node.random:
            rdata = node.random.data
            if rdata not in cmap:
                rnode = Node(rdata+1) # +1 to check if it's a new list
                cmap[rdata] = rnode
            rnode = cmap[rdata]

            clone.random = rnode
        prev = clone
        node = node.next

    return head

printlist(clone_random(head))
