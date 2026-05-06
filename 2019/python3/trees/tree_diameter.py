#!/usr/bin/env python3

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diameter2(root):
    if not root:
        #print("none dt as: ", 0)
        return -1, 0

    lh, ld = diameter2(root.left)
    rh, rd = diameter2(root.right)

    my_dt = 0
    if lh != -1:
        my_dt = ld+1
    if rh != -1:
        my_dt += rd+1

    #print("returning dt for:", root.data, ", as: ", max(ld, rd, my_dt))
    return 1, max(ld, rd, my_dt)



def diameter(root):
    
    if not root:
        return -1, 0

    left_ht, left_dt = diameter(root.left)
    right_ht, right_dt = diameter(root.right)

    my_ht = max(left_ht, right_ht) + 1
    my_dt = left_dt+right_dt+2

    act_dt = max(left_dt, my_dt, right_dt)
    return my_ht, act_dt

def insert_tree(root, data):

    while root:
        if root.data > data:
            if not root.left:
                root.left = Node(data)
                break
            root = root.left
        elif root.data < data:
            if not root.right:
                root.right = Node(data)
                break
            root = root.right
        else:
            root.data = data
            break

    return


def create_tree(l):
    root = Node(l[0])

    for data in l[1:]:
        insert_tree(root, data)

    return root

def print_level_tree(root):
    q = []
    q.append([root, 0])
    prev_level = 0

    print("level order: [")
    while q:
        node, level = q.pop(0)
        if node:
            if level != prev_level:
                prev_level = level
                print()
            print(node.data, end=' ')
            q.append([node.left, level+1])
            q.append([node.right, level+1])
    print()

def main():
    #l = [13, 2, 8, 9, 10, 5, 4, 3, 14]
    #l = [10, 6, 9, 8, 7, 11, 13, 12]
    l = [10]
    root = create_tree(l)
    print_level_tree(root)
    ht, dt = diameter(root)
    print("Height: ", ht, ", Diameter:", dt)
    print("Diameter2:", diameter2(root))


if __name__ == '__main__':
    main()

