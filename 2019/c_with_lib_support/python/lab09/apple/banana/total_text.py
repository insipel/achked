#!/usr/bin/env python
"""Provides a TotalText function, which adds up all the
numbers in the text that it receives."""

import string  
punctuation_except_decimal = string.punctuation.replace('.', '')

def TotalText(text, total=0):
    """Returns the sum of all the numbers in the text."""

    words = text.split()
    for word in words:
        word = word.strip(punctuation_except_decimal)
        word = word.rstrip('.')
        try:
            num = float(word)
        except ValueError:
            pass
        else:
            total += num
    return total

def main():
    print "Total =",
    print TotalText("""Here is 1. Add 2 makes 3 or maybe 12, 
depending on how you operate.

You might like 2.2 and that's enough unless you like "8.8" or 
maybe 1 more or maybe 87. . .5""")

if __name__ == '__main__':
    main()
