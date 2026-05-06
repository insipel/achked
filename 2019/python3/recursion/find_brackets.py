#!/usr/bin/env python3

def find_brackets(n, l, r, s):
    #print('n:', n, ", l:", l, ", r:", r, ", s:", s)
    if l == n and r == n:
        print(''.join(c for c in s))
        return

    if l<n:
        s.append('(')
        find_brackets(n, l+1, r, s)
        s.pop()

    if r<l:
        s.append(')')
        find_brackets(n, l, r+1, s)
        s.pop()

def main():
    s = []
    n = 4
    find_brackets(n, 0, 0, s)

if __name__ == '__main__':
    main()

