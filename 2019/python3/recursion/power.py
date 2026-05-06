#!/usr/bin/env python3

def power(a, b):
    print('b:', b)
    if b == 0:
        return 1

    if b < 0:
        b = -b
        a = 1/a

    temp = power(a, b//2)
    if b % 2 == 0:
        return temp * temp
    else:
        return a * temp * temp

def main():
    a = 4
    b = -2
    print(power(a, b))

if __name__ == '__main__':
    main()

