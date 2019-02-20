#!/usr/bin/env python3

def min_coin_change(A, D):
    res = [float('inf')] * (A + 1)

    res[0] = 0
    for a in range(1, A+1):
        temp = float('inf')

        for d in D:
            if d <= a:
                temp = min(temp, res[a-d])
                #print("a:", a, ", d:", d, ", temp:", temp, ", res[",
                #        (a-d), "]:", res[a-d])
        res[a] = temp + 1

    print(res)
    return res

def print_res(A, D, res):
    print(A, " is made up with: ")

    l = []
    a = A
    while a > 0:
        temp = float('inf')
        #temp_coin = 0

        for d in D:
            if d <= a and temp > res[a-d]:
                print("a:", a, ", coin: ", d)
                temp = res[a-d]
                temp_coin = d

        if temp == float('inf'):
            print("No valid solution, ", l)
            return
        else:
            a = a - temp_coin
            l.append(temp_coin)

    print(l)

def main():
    A = 13
    D = [3, 8, 7, 9]
    print("Target:", A)
    print("Coins:", D)
    res = min_coin_change(A, D)
    print_res(A, D, res)

if __name__ == '__main__':
    main()

