#!/usr/bin/env python3

def count_path_blocked(grid):
    m = len(grid)
    n = len(grid[0])
    res = [ [0] * (n+1) for _ in range(m+1)]

    for r in range(m-1, -1, -1):
        for c in range(n-1, -1, -1):

            if grid[r][c] == 0:
                res[r][c] = 0
            elif r == m-1 and c == n -1:
                res[r][c] = 0 if grid[r][c] == 0 else 1
            else:
                res[r][c] = res[r+1][c] + res[r][c+1]

    for i in range(m+1):
        print(res[i])
    return res[0][0]

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
            [4, 0, 11, 1]]
    print(count_path_blocked(grid))

if __name__ == '__main__':
    main()

