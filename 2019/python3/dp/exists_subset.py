#!/usr/bin/env python3

def exists_subset(K, S):
    n = len(S)
    res = [ [0] * (K+1) for _ in range(n+1)]

    for i in range(n, -1, -1):
        for k in range(K+1):
            if k == 0:
                res[i][k] = True
            elif i == n:
                res[i][k] = False
            else:
                res[i][k] = res[i+1][k]
                if k >= S[i]:
                    res[i][k] |= res[i+1][k - S[i]]

    for i in range(n+1):
        print(res[i])

    return res[0][K]

def main():
    K = 11
    S = [3, 4, 7, 9, 8]
    print("subset with sum ", K, "exists" if exists_subset(K, S) else "doesn't exist")

if __name__ == '__main__':
    main()

