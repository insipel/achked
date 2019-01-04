#!/usr/bin/env python
"""Provides CountVowels, a vowel counting function."""
import string
def CountVowels(phrase):
    """Returns the number of vowels in the "phrase" input.
    'y' is not counted if it is the first character.
        is not counted if it is preceded by a vowel.
        is counted in 'ying' if it is at the end of the word.
        is counted at the end of the word, if preceded by
           a consonant.
        is counted if it is preceded and followed by a
           consonant.
     """
    ALWAYS_VOWELS = "aeiou"
    spurious = string.punctuation + '0123456789_'
    count = 0
    for word in phrase.lower().split():
        word = word.strip(spurious)
        l_word = len(word)
        for index, char in enumerate(word):
            if char in ALWAYS_VOWELS:
                count += 1
                continue
            if char != 'y' or index == 0:
                # now, char is 'y' and not the first char
                continue
            if word[index-1] in ALWAYS_VOWELS:
                # preceded by a vowel
                continue
            if word.endswith('ying') and index == l_word - 4:
                count += 1
                continue
            # now, it is a 'y' preceded by a consonant
            if (index == l_word - 1   # at end of word
                or word[index+1] not in ALWAYS_VOWELS):
                # or followed by a consonant
                count += 1
                continue
    return count
def main():
    """Tests the CountVowels function."""
    for test in (
        """Math, science, history, unraveling the mysteries,
        that all started with the big bang!""",
        "boy way hey myth satyr fly flying spying",):
        print CountVowels(test), test

if __name__ == "__main__":
    main()
"""
$ lab06_5.py
24 Math, science, history, unraveling the mysteries,
        that all started with the big bang!
11 boy way hey myth satyr fly flying spying
$ """ 


