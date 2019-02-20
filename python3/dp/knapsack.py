#!/usr/bin/env python3

def knapsack(v, w):
    n = len(v)

    # columns -> wt
    # rows -> i in 'v'
    res = [[0] * (w + 1) for _ in range(n+1)]

    # for all res[i][0] = 0
    # for all res[w][0] = 0
    # f(i, w): max val starting at idx i with wt w to fill.

    for i in range(n-1, -1, -1):
        v_i = v[i][0]
        w_i = v[i][1]

        print("i: ", i, ", v_i:", v_i, ", w_i:", w_i) 
        for cur_wt in range(1, w+1):

            #if i == n - 1:
            #    res[i][cur_wt] = 0
            #elif w_i == 0:
            #    res[i][cur_wt] = 0
            #elif cur_wt > w_i:
            print("cur_wt:", cur_wt)
            if w_i > cur_wt:
                res[i][cur_wt] = res[i+1][cur_wt]
                print("skip: res[i+1][cur_wt]:", res[i+1][cur_wt])
            else:
                res[i][cur_wt] = max(res[i+1][cur_wt],
                                  res[i+1][cur_wt - w_i] + v_i)
                print("pick: res[i+1][cur_wt]:", res[i+1][cur_wt],
                ", res[i+1][cur_wt - w_i] + v_i:", res[i+1][cur_wt - w_i] + v_i)

    return(res)

def main():
    v = [(4,3), (2, 2), (4, 3), (1, 1), (3, 5), (6, 2), (7, 5)]
    w = 5
    print(knapsack(v, w))

if __name__ == '__main__':
    main()
 
