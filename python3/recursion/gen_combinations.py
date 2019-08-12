#!/usr/bin/env python3

def comb(l, res, lidx, k):
    if k == 0:
        print(''.join(c for c in res))
        return

    for i in range(lidx, len(l)):
        res.append(l[i])
        #print(res, k)
        comb(l, res, i+1, k-1)
        res.pop()

def main():
    s = "abcd"
    k = 3
    comb(s, [], 0, k)

if __name__ == '__main__':
    main()

