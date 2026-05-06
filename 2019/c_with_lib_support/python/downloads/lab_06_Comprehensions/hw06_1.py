#!/usr/bin/env python
"""Provides SeparateThousands."""

def SeparateThousands(number, decimal_digits=None):
    """Returns the string version of the number,
    with commas.

    decimal_digits, if given, will be the number of 
    digits to the right of the decimal in the result.
    """
    sign = ''
    if number < 0:
        sign = '-'
        number = -number

    if decimal_digits == None:
        formatted = str(number)
    else:
        formatted = "%.*f" % (decimal_digits, number)

    parts = formatted.split('.')
    decimal = ""
    if len(parts) == 2:
        decimal = "." + parts[1]
    whole = parts[0]
    reversed_answer = []
    for index, char in enumerate(reversed(whole)):
        if index % 3 == 0 and index != 0:
            reversed_answer += [',']
        reversed_answer += [char]
    whole = ''.join(reversed(reversed_answer))
    return sign + whole + decimal

def main():
    """Testing for SeparateThousands function."""
    for number in (100, 100.1545, 12345.5452, 1200, 1200.23,
                  1200.1, 123456789.556, .087):
        for sign in (1, -1):
            for digits in (None, 0, 1, 2, 8):
                value = sign * number
                print "SeparateThousands(%s, %s) --> '%s'" % (
                    value, digits, SeparateThousands(value, digits))

if __name__ == '__main__':            
    main()
"""
$ hw06_1.py
SeparateThousands(100, None) --> 100
SeparateThousands(100, 0) --> 100
SeparateThousands(100, 1) --> 100.0
SeparateThousands(100, 2) --> 100.00
SeparateThousands(100, 8) --> 100.00000000
SeparateThousands(-100, None) --> -100
SeparateThousands(-100, 0) --> -100
SeparateThousands(-100, 1) --> -100.0
SeparateThousands(-100, 2) --> -100.00
SeparateThousands(-100, 8) --> -100.00000000
SeparateThousands(100.1545, None) --> 100.1545
SeparateThousands(100.1545, 0) --> 100
SeparateThousands(100.1545, 1) --> 100.2
SeparateThousands(100.1545, 2) --> 100.15
SeparateThousands(100.1545, 8) --> 100.15450000
SeparateThousands(-100.1545, None) --> -100.1545
SeparateThousands(-100.1545, 0) --> -100
SeparateThousands(-100.1545, 1) --> -100.2
SeparateThousands(-100.1545, 2) --> -100.15
SeparateThousands(-100.1545, 8) --> -100.15450000
SeparateThousands(12345.5452, None) --> 12,345.5452
SeparateThousands(12345.5452, 0) --> 12,346
SeparateThousands(12345.5452, 1) --> 12,345.5
SeparateThousands(12345.5452, 2) --> 12,345.55
[30 lines deleted]
SeparateThousands(-1200.1, None) --> -1,200.1
SeparateThousands(-1200.1, 0) --> -1,200
SeparateThousands(-1200.1, 1) --> -1,200.1
SeparateThousands(-1200.1, 2) --> -1,200.10
SeparateThousands(-1200.1, 8) --> -1,200.10000000
SeparateThousands(123456789.556, None) --> 123,456,789.556
SeparateThousands(123456789.556, 0) --> 123,456,790
SeparateThousands(123456789.556, 1) --> 123,456,789.6
SeparateThousands(123456789.556, 2) --> 123,456,789.56
SeparateThousands(123456789.556, 8) --> 123,456,789.55599999
SeparateThousands(-123456789.556, None) --> -123,456,789.556
SeparateThousands(-123456789.556, 0) --> -123,456,790
SeparateThousands(-123456789.556, 1) --> -123,456,789.6
SeparateThousands(-123456789.556, 2) --> -123,456,789.56
SeparateThousands(-123456789.556, 8) --> -123,456,789.55599999
SeparateThousands(0.087, None) --> '0.087'
SeparateThousands(0.087, 0) --> '0'
SeparateThousands(0.087, 1) --> '0.1'
SeparateThousands(0.087, 2) --> '0.09'
SeparateThousands(0.087, 8) --> '0.08700000'
SeparateThousands(-0.087, None) --> '-0.087'
SeparateThousands(-0.087, 0) --> '-0'
SeparateThousands(-0.087, 1) --> '-0.1'
SeparateThousands(-0.087, 2) --> '-0.09'
SeparateThousands(-0.087, 8) --> '-0.08700000'
"""
