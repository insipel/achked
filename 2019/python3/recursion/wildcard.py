#!/usr/bin/env python3

def wildcard(s, res, idx):

    if idx == len(s):
        print(res)
        return

    #for i in range(idx, len(s)):
    i = idx
    cur_char = s[i]

    if cur_char == '?':
        wildcard(s, res+'0', i+1)
        wildcard(s, res+'1', i+1)
    else:
        res += cur_char
        wildcard(s, res, i+1)

def main():
    #s = "?"
    #s = "a?"
    s = "a?bc?d"
    wildcard(s, "", 0)

if __name__ == "__main__":
    main()

