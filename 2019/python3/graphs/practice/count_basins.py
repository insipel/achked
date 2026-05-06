#!/usr/bin/env python3

def count_basins(grid):
    r = len(grid)
    c = len(grid[0])

    basin_res = [ [-1 for _ in range(c)] for _ in range(r)]
    
    hmap = {}
    for i in range(r):
        for j in range(c):
            ht = grid[i][j]
            if ht in hmap:
                hmap[ht].append((i, j))
            else:
                hmap[ht] = [(i, j)]
    i = 0
    hlist = [0] * len(hmap)
    for ht in hmap:
        hlist[i] = ht
        i += 1
    hlist.sort()
    #print(hlist)


    basin_cnt = 0
    for ht in hlist:
        for i, j in hmap[ht]:
            if basin_res[i][j] == -1:
                basin_res[i][j] = basin_cnt
                basin_cnt += 1
            set_nbr_sinks(i, j, r, c, basin_res)

    #for i in range(len(basin_res)):
        # print(basin_res[i])

    basin_count = [0 for _ in range(basin_cnt)]
    for i in range(r):
        for j in range(c):
            basin_count[basin_res[i][j]] += 1

    #print(basin_count)
    basin_count.sort()
    return(basin_count)

def set_nbr_sinks(i, j, r, c, basin_res):
    nxt = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    res = basin_res[i][j]

    for dr, dc in nxt:
        nr = i + dr
        nc = j + dc

        if 0<=nr<r and 0<=nc<c and basin_res[nr][nc] == -1:
            basin_res[nr][nc] = res

grid = [
        [2, 3, 6, 2],
        [9, 5, 1, 7],
        [3, 8, 9, 3],
        [2, 1, 4, 1]]

res = count_basins(grid)
print("basins are of size:", res)
