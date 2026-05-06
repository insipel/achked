#!/usr/bin/env python3

def idx_min_coin(T, D):
    n = len(D)
    res = [[float('inf')] * (T+1) for _ in range(n+1)]

    for i in range(n, -1, -1):
        for t in range(T+1):
            if t == 0:
                res[i][t] = 0
            #elif i == n: Not needed due to the initialization we did
            #    res[i][t] == float('inf')
            elif i == n:
                res[i][t] = float('inf')
            else:
                res[i][t] = res[i+1][t]
                if t >= D[i]:
                    res[i][t] = min(res[i+1][t], 1+res[i][t-D[i]])

                # increase number of coins only if picked a coin and
                # didn't skip the cur coin. If we skipped the current
                # coin, then don't count it against the number of
                # coins.
                #if res[i][t] != res[i+1][t]:
                #    res[i][t] += 1
    
    for i in range(n+1):
        print(res[i])
    return res[0][T]
    
def main():
    #T = 13
    T = 10 # Would 3, 7 and 7, 3 counting twice make an issue? Current
           # code does
    D = [3, 8, 7, 9]
    print(idx_min_coin(T, D))

if __name__ == '__main__':
    main()

