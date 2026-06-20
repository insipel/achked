#!/usr/bin/env python
"""MakeMoneyString(amount) returns a money representation
of the amount.
"""
import hw06_1 as thousands

def MakeMoneyString(amount):
    """Returns a money representation of the amount."""

    thousands_str = thousands.SeparateThousands(amount,
                                                 2)
    if thousands_str[0] == '-':
        return '-$' + thousands_str[1:]
    return '$' + thousands_str

def main():
    print MakeMoneyString(-123.21)
    print MakeMoneyString(3)
    print MakeMoneyString(14.3123)
    print MakeMoneyString(1234567.89)
    print MakeMoneyString(-88.88)

if __name__ == '__main__':
    main()
"""
$ hw06_2.py
-$123.21
$3.00
$14.31
$1,234,567.89
-$88.88
$"""
