#!/usr/bin/env python

""" Stack class """

class Stack:

    def __init__(self):
        self.stack = []
        print "Created stack"

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        elem = 0
        try:
            elem = self.stack.pop()
        except IndexError:
            print "Empty Stack"

        return elem


def main():
    stack = Stack()
    stack.push(12)
    stack.push(16)
    stack.push(1)
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.pop()

if __name__ == '__main__':
    main()

