#!/usr/bin/env python3

def print_dg(g):
    m = len(g)
    n = len(g[0])

    for i in range(m+n):

        if i < m:
            r = i
            c = 0
        else:
            c += 1

        r1 = r
        c1 = c

        while r1 >= 0 and c1 < n:
            print(g[r1][c1], end = ', ')
            r1 -= 1
            c1 += 1
        print()


def main():
    g = [[0, 1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10, 11],
         [12, 13, 14, 15, 16, 17],
         [18, 19, 20, 21, 22, 23]]
    print(g)
    print_dg(g)

if __name__ == '__main__':
    main()

