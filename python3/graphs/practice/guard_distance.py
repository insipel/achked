#!/usr/bin/env python3

def get_neighbors(curr_r, curr_c, r, c):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    output = []

    for dr, dc in moves:
        nr = curr_r + dr
        nc = curr_c + dc

        if 0<=nr<r and 0<=nc<c:
            output.append((nr, nc))

    return output

def guard_distance(grid):
    r = len(grid)
    c = len(grid[0])

    res = [ [-1 for _ in range(c)] for _ in range(r)]

    q = []

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'G':
                res[i][j] = 0
                q.append((i, j))

    while q:
        curr_r, curr_c = q.pop(0)

        for nr, nc in get_neighbors(curr_r, curr_c, r, c):
            if grid[nr][nc] == 'O' and res[nr][nc] == -1:
                res[nr][nc] = res[curr_r][curr_c] + 1
                q.append((nr, nc))

    return res


grid = [["O", "O", "G", "O"], ["O", "W", "O", "O"],
["O", "O", "O", "G"],
["G", "O", "W", "O"],
["O", "O", "G", "O"]]
res = guard_distance(grid)
for i in range(len(grid)):
    print(grid[i], "--", res[i])

