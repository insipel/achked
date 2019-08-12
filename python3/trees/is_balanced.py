#!/usr/bin/env python3

from tree_creation import *

def is_balanced(root):
    if not root:
        return True, -1

    is_left_bal,  lh = is_balanced(root.left)
    if not is_left_bal:
        return False, -1

    is_right_bal, rh = is_balanced(root.right)
    if not is_right_bal:
        return False, -1

    if abs(lh - rh) > 1:
        return False, -1

    h = max(lh, rh)
    return True, h+1

def main():
    #l = [10, 6, 9, 8, 11, 13, 12, 7]
    l = [10, 6, 5, 9, 11, 13]
    root = create_tree(l)
    print_level_tree(root)
    print("Tree height is:", is_balanced(root))

if __name__ == '__main__':
    main()

