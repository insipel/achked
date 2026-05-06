#!/usr/bin/env python3

def maxpath_dp(grid):
    m = len(grid)
    n = len(grid[0])

    res = [[float('-inf')] * (n + 1) for _ in range(m+1)]

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            max_val = max(res[i+1][j], res[i][j+1])
            #if max_val == float('-inf'):
            if i == m - 1 and j == n - 1: # This is better in line with RR
                res[i][j] = grid[i][j]
            else:
                res[i][j] = grid[i][j] + max_val
    return res

def print_maxpath(grid, res):
    print(grid[0][0])

    i = j = 0
    m = len(grid)
    n = len(grid[0])

    while i < m -1  or j < n -1 :
        if res[i+1][j] > res[i][j+1]:
            print(grid[i+1][j])
            i = i + 1
        else:
            print(grid[i][j+1])
            j = j+1

def main():
    #grid = [[1, 2, 3, 4],
    #        [5, 0, 9, 2],
    #        [1, 7, 3, 5],
    #        [12, 6, 2, 3],
    #        [4, 2, 11, 1]]
    grid = [[1, 2, 3, 4],
            [-5, 0, 9, 2],
            [1, 7, 3, 5],
            [-12, 6, 2, 3],
            [4, 2, 11, 1]]
    res = maxpath_dp(grid)
    #print(res)
    print(res[0][0])
    for i in range(len(res)):
        print(res[i])
    print_maxpath(grid, res)

if __name__ == '__main__':
    main()

