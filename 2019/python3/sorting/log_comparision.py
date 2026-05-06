#!/usr/bin/env python3

from math import *

# Compare two logarithmic expressions:
# 1) n * log(k) for fixed n and varying k
# 2) k * log(n) for fixed k and varying n
# This helps illustrate how the two forms grow differently as n or k increases.

def main():
    K = 10
    N = 100

    print("nlg(k):")
    for n in range(1, N, 10):
        # Fix n and compute n * log(k) for increasing k
        print("n:", n, end=": ")
        for k in range(1, K):
            print(n * log(k), end = ", ")
        print()

    print()
    print()
    print()
    print("klg(n):")
    for k in range(1, K):
        # Fix k and compute k * log(n) for increasing n
        print("k:", k, end=": ")
        for n in range(1, N, 10):
            print(k * log(n), end = ", ")
        print()

if __name__ == '__main__':
    main()

