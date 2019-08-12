#!/usr/bin/env python3

class A:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        print("Created A")

    def print_me(self):
        print("My name is ", self.name)
        print("My data is ", self.data)

class B(A):
    def __init__(self, name, data, time=10):
        A.__init__(self, name, data)
        self.time = time
        print("Created B")

    def print_me(self):
        print("I am ", self.name, " with data: ", self.data)

a = A("nameA", 10)
b = B("nameB", 20)
a.print_me()
b.print_me()

