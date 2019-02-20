#!/usr/bin/env python3

def rob_max(v):
    n = len(v)
    res = [0] * (n + 2)

    for i in range(2, n+2):
        vIdx = i - 2
        res[i] = max(res[i-2]+v[vIdx], res[i-1])

    return res

def main():
    v = [2, 10, 200, 190, 30, 80, 15]
    print(rob_max(v))

if __name__ == '__main__':
    main()

