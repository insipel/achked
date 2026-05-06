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
#n4 = Node(4)
#n5 = Node(5)
#n6 = Node(6)
#n7 = Node(7)
#n8 = Node(8)
#n9 = Node(9)
n1.next = n2
#n2.next = n3
#n3.next = n4
#n4.next = n5
#n5.next = n6
#n6.next = n7
#n7.next = n8
#n8.next = n9
head = n1
printlist(head)

def swap_kth(head, k):
    print("swap_kth", head.data, k)
    if not k: return head

    prev1 = None
    ptr1 = head
    k = k - 1
    while ptr1.next and k:
        prev1 = ptr1
        ptr1 = ptr1.next
        k -= 1

    #print(k)
    if k:
        return head

    temp = ptr1
    prev2 = None
    ptr2 = head

    while temp.next:
        prev2 = ptr2
        ptr2 = ptr2.next
        temp = temp.next

    if prev1 != None:
        prev1.next = ptr2
    else:
        head = ptr2

    if prev2 != None:
        prev2.next = ptr1
    else:
        head = ptr1


    temp = ptr1.next
    ptr1.next = ptr2.next
    ptr2.next = temp

    return head

printlist(swap_kth(head, 2))
