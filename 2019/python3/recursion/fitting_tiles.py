#!/usr/bin/env python3

def tiles(n):
    res = [0] * (n+1)
    res[1] = 1
    res[2] = 2

    for i in range(3, n+1):
        res[i] = res[i-1] + res[i-2]

    return res[n]

print("3:", tiles(3))
print("4:", tiles(4))
print("5:", tiles(5))
print("6:", tiles(6))

# Block: n x m
# tile : 1 x m
def tiles(n, m):
    res = [0] * (n+1)

    for i in range(1,n+1):
        if 1 <= i and i < m:
            res[i] = 1 # Placing all times just vertically
        elif i == m:
            res[i] = 2 # Placing once horizaontally and one vertically
        else:
            # Place one tile vertically, get the result for i - 1 len 
            # Place m tiles horizontally and get the result for i - m len
            res[i] = res[i - 1] + res[i - m]

    return res[n]

print("2, 3:", tiles(2, 3))
print("3, 2:", tiles(3, 2))
print("4, 4:", tiles(4, 4))
print("5, 4:", tiles(5, 4))
print("6, 3:", tiles(6, 3))
print("7, 4:", tiles(7, 4))


