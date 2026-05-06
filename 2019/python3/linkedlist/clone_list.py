#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def printlist(head):
    print("List: [", end = '')
    while head:
        print(head.data, end=",")
        head = head.next
    print("]")

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
#n5 = Node(5)
#n6 = Node(6)
#n7 = Node(7)
#n8 = Node(8)
#n9 = Node(9)
n1.next = n2
n2.next = n3
n3.next = n4
#n4.next = n5
#n5.next = n6
#n6.next = n7
#n7.next = n8
#n8.next = n9
head = n1
printlist(head)

def clone_list(node):
    prev = None
    head = None

    while node:
        clone = Node(node.data)
        node = node.next
        if not prev:
            head = clone
        else:
            prev.next = clone
        prev = clone
            
    clone.next = None

    return head

clone_head = clone_list(head)
printlist(clone_head)
print(head == clone_head)

