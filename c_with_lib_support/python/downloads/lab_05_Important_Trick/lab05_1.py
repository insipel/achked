#!/usr/bin/env python
"""Provides CountVowels, a vowel counting function.
"""
def CountVowels(text):
    """Returns the number of vowels in the "text" input,
    excluding 'y's.
    """
    count = 0
    for character in text.lower():
        if character in "aeiou":
            count += 1
    return count

def main():
    """Tests the CountVowels function."""
    for test in ("!", "Math, science, history, unraveling the"
                 " mysteries, that all started with the big"
                 " bang!", ""):
        print CountVowels(test)
if __name__ == "__main__":
    main()
"""
$ lab05_1.py
0
22
0
$
"""
