#!/usr/bin/env python3

def safe_place(grid, c, r):
    for i in range(c):
        if grid[i] == r:
            return False
        if abs(grid[i] - r) == abs(c - i):
            return False
    return True

def n_queens(grid, c):
    if c == len(grid):
        print(grid)
        return

    for r in range(len(grid)):
        if (safe_place(grid, c, r)):
            grid[c] = r
            n_queens(grid, c+1)
            grid[c] = -1

def main():
    n = 4
    grid = [-1] * n
    n_queens(grid, 0)

if __name__ == '__main__':
    main()

