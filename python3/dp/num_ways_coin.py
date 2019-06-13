#!/usr/bin/env python3

def count_coin_change(T, D):
    n = len(D)
    res = [[0] * (T+1) for _ in range(n+1)]

    for i in range(n, -1, -1):

        for t in range(T+1):
            if i == n:
                res[i][t] = 0
            elif t == 0:
                res[i][t] = 1
            else:
                print("d[i] <= t", D[i], t)
                res[i][t] = res[i+1][t]
                if D[i] <= t:
                    res[i][t] += res[i][t - D[i]]

    for i in range(n+1):
        print(res[i])
    return res[0][T]

def main():
    #T = 13
    T = 14
    D = [3, 8, 7, 9]
    print(count_coin_change(T, D))

if __name__ == '__main__':
    main()

