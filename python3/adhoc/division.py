#!/usr/bin/env python3

def division_brute(a, b):
    q = 0

    a = a - b
    while a > 0:
        q += 1
        a = a - b
    print("quotient: ", q)

def division_shift(a, b):
    q = 0
    shift_count = 0

    while (b << (shift_count + 1) <= a):
            shift_count += 1

    while a >= b:

        while (b << shift_count > a):
            shift_count -= 1

        q += (1 << shift_count)
        a -= (b << shift_count)

    print("quotient: ", q)

#division_brute(21, 5)
#division_shift(21, 5)
division_shift(37, 3)
division_shift(37, 4)

