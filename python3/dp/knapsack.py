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

        #print("i: ", i, ", v_i:", v_i, ", w_i:", w_i) 
        for cur_wt in range(1, w+1):

            #if i == n - 1:
            #    res[i][cur_wt] = 0
            #elif w_i == 0:
            #    res[i][cur_wt] = 0
            #elif cur_wt > w_i:
            #print("cur_wt:", cur_wt)
            if w_i > cur_wt:
                res[i][cur_wt] = res[i+1][cur_wt]
                #print("skip: res[i+1][cur_wt]:", res[i+1][cur_wt])
            else:
                res[i][cur_wt] = max(res[i+1][cur_wt],
                                  res[i+1][cur_wt - w_i] + v_i)
                #print("pick: res[i+1][cur_wt]:", res[i+1][cur_wt],
                #", res[i+1][cur_wt - w_i] + v_i:", res[i+1][cur_wt - w_i] + v_i)

    for i in range(len(res)):
        print(res[i])
    return(res[0][w])

# Cleaner implementation of above routine
def fill_wt(l, W):
    n = len(l)

    res = [[-1 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(n, -1, -1):
        if i != n:
            # These values will only be use for i = n-1 onwards
            item_val = l[i][0]
            item_wt  = l[i][1]

        for bag_wt in range(W+1):
            if i == n or bag_wt == 0:
                res[i][bag_wt] = 0
            elif item_wt > bag_wt:
                res[i][bag_wt] = res[i+1][bag_wt]
            else:
                res[i][bag_wt] = max(res[i+1][bag_wt],
                                     item_val + res[i+1][bag_wt - item_wt])

    for i in range(len(res)):
        print(res[i])
    return(res[0][W])

def main():
    v = [(4,3), (2, 2), (4, 3), (1, 1), (3, 5), (6, 2), (7, 5)]
    w = 5
    print(knapsack(v, w))
    print(fill_wt(v, w))

if __name__ == '__main__':
    main()
 
