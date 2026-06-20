#!/usr/bin/env python

import tree_def

class FruitTree(tree_def.Tree):

    def __init__(s, fruit_type):
        tree_def.Tree.__init__(s, 20)
        s.fruit_type = fruit_type
        pass

    def Print(s):
        tree_def.Tree.Print(s)
        print "Eat my %s" % s.fruit_type

def main():
    ft1 = FruitTree("apple")
    ft2 = FruitTree("banana")
    ft3 = FruitTree("fig")
    ft1.Print()
    ft2.Print()
    ft3.Print()

if __name__ == '__main__':
    main()

