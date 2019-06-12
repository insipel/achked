#!/usr/bin/env python3

from math import *

def main():
    K = 10
    N = 100

    print("nlg(k):")
    for n in range(1, N, 10):
        print("n:", n, end=": ")
        for k in range(1, K):
            print(n * log(k), end = ", ")
        print()

    print()
    print()
    print()
    print("klg(n):")
    for k in range(1, K):
        print("k:", k, end=": ")
        for n in range(1, N, 10):
            print(k * log(n), end = ", ")
        print()

if __name__ == '__main__':
    main()

