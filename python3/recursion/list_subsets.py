#!/usr/bin/env python3

def list_subsets(s, i, l):
    if i == len(s):
        print(''.join(c for c in l))
        return

    list_subsets(s, i+1, l)
    l.append(s[i])
    list_subsets(s, i+1, l)
    #l.remove(s[i])
    l.pop()

def main():
    s = 'abc'
    l = []
    list_subsets(s, 0, l)

if __name__ == '__main__':
    main()

