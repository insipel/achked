#!/usr/bin/env python3

def rob_max(v):
    n = len(v)
    res = [0] * (n + 2)

    for i in range(2, n+2):
        vIdx = i - 2
        res[i] = max(res[i-2]+v[vIdx], res[i-1])

    print(res[n+1])
    return res

def rob_max2(v):
    n = len(v)
    res = [0] * (n + 2)

    for i in range(0, n):
        res[i+2] = max(res[i]+v[i], res[i+1])

    print(res[n+1])
    return res

def main():
    v = [2, 10, 200, 190, 30, 80, 15]
    print(rob_max(v), rob_max2(v))

if __name__ == '__main__':
    main()

