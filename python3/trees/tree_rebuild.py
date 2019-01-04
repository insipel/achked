#!/usr/bin/env python3

from tree_creation import create_tree, print_level_tree, print_tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rebuild_tree(inStr, inSt, inEnd, preStr, preSt, preEnd):
    if inSt > inEnd or preSt > preEnd:
        return None

    root = Node(preStr[preSt])
    k = 0
    for i in range(inEnd+1):
        if root.data == inStr[i]:
            k = i
            break

    root.left = rebuild_tree(inStr, inSt, k - 1, preStr, preSt+1,
            preSt + k - inSt)
    root.right = rebuild_tree(inStr, k + 1, inEnd, preStr, preSt + k +
            1 - inSt, preEnd)

    return root


def main():
    #l = [6, 3, 10, 2, 5, 7, 12, 1, 4, 8, 11, 14]

    #inStr = [1, 2]
    #preStr = [2, 1]
    inStr = [1,2, 3, 5]
    preStr = [3, 1, 2, 5]

    root = rebuild_tree(inStr, 0, len(inStr) - 1, preStr, 0, len(preStr) - 1)
    print_level_tree(root)
    print_tree(root)

if __name__ == '__main__':
    main()

