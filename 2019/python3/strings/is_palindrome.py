#!/usr/bin/env python3

def is_palindrome(s):
    i, j = 0, len(s) - 1

    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def main():
    s = "abba"
    print("is ", s, " a palindrome? ", is_palindrome(s))

if __name__ == '__main__':
    main()

