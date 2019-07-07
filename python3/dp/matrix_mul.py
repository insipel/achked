#!/usr/bin/env python3

def matrix_mul(m):
    n = len(m)

    res = [[0 for _ in range(n)] for _ in range(n)]
    cut_idx = [[0 for _ in range(n)] for _ in range(n)]

    for group_sz in range(2, n+1):
        for i in range(n - group_sz + 1):
            j = i + group_sz - 1

            res[i][j] = float('inf')

            for k in range(i, j):
                #print("i:", i, ", j:", j, ", k:", k)
                #print("m[",i,"]:(",m[i].r,m[i].c, "), m[",k,"]:(",m[k].r,m[k].c,
                #      "), m[",j,"]:(",m[j].r,m[j].c)

                q = res[i][k] + res[k+1][j] + m[i].r * m[k].c * m[j].c

                if q < res[i][j]:
                    res[i][j] = q
                    cut_idx[i][j] = k

        for r in range(n):
            print(res[r])
        print("============")

    for i in range(n):
        print(cut_idx[i])
    print_paran(cut_idx, 0, n-1)
    print()

def print_paran(s, i, j):
    if i == j:
        print("M", i, end = '')
    else:
        print("(", end = "")
        print_paran(s, i, s[i][j])
        print_paran(s, s[i][j]+1, j)
        print(")", end = "")

class Matrix:
    def __init__(self, r, c):
        self.r = r
        self.c = c

M0 = Matrix(30, 35)
M1 = Matrix(35, 15)
M2 = Matrix(15, 5)
M3 = Matrix(5, 10)
M4 = Matrix(10, 20)
M5 = Matrix(20, 25)
m = [M0, M1, M2, M3, M4, M5]
matrix_mul(m)

