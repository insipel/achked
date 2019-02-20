#!/usr/bin/env python3

def nth_fib(n):
    fib = [0] * n
    fib[0] = 0
    fib[1] = 1

    print(fib[0], ", ", fib[1], end=", ")
    for i in range(2, n):
        fib[i] = fib[i-2] + fib[i-1]
        print(fib[i], end=", ")

    print()
    return fib[n-1]

def main():
    n = 20
    print(nth_fib(n))

if __name__ == '__main__':
    main()

