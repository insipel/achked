#!/usr/bin/env python3

def num_subsets(K, S):
    n = len(S)
    res = [[0] * (K+1) for _ in range(n+1)]

    for i in range(n, -1, -1):
        for k in range(K+1):
            if k == 0:
                res[i][k] = 1
            elif i == n:
                res[i][k] = 0
            else:
                res[i][k] = res[i+1][k]
                if k >= S[i]:
                    res[i][k] += res[i+1][k - S[i]]

    for i in range(n+1):
        print(res[i])
    return res[0][K]

def main():
    K = 12
    S = [3, 2, 5, 8, 7, 9]
    print(num_subsets(K, S))

if __name__ == '__main__':
    main()

