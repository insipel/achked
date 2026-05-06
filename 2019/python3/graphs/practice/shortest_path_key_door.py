#!/usr/bin/env python3

max_key = 10 # a to j
max_mask = 1 << max_key

def shortest_path(grid):
    r, c = len(grid), len(grid[0])

    start, end = get_start_end_cell(grid)
    sr, sc = start
    er, ec = end

    state = [[[float('inf') for _ in range(max_mask)]
                 for _ in range(c)]
                 for _ in range(r)]

    parent = [[[0 for _ in range(max_mask)]
                  for _ in range(c)]
                  for _ in range(r)]

    visited = [[[False for _ in range(max_mask)]
                       for _ in range(c)]
                       for _ in range(r)]

    bfs(grid, start, state, parent, visited)

    length = float('inf')
    key_ring = 0
    for i in range(max_mask):
        if length > state[er][ec][i]:
            length = state[er][ec][i]
            key_ring = i

    return build_path(state, parent, key_ring, start, end)


def is_start(ch):
    return ch == '@'

def is_stop(ch):
    return ch == '+'

def is_land(ch):
    return ch == '.'

def is_water(ch):
    return ch == '#'

def is_key(ch):
    return(0 <= (ord(ch) - ord('a')) < max_key)
    #return(ch in 'abcdefghij')

def is_door(ch):
    return(0 <= (ord(ch) - ord('A')) < max_key)
    #return(ch in 'ABCDEFGHIJ')

def can_open_door(door, key_ring):
    offset = ord(door) - ord('A')
    return (key_ring >> offset) & 1

def add_nbr_to_q(to_r, to_c, to_key_ring, from_node, parent, state,
        visited, q):
    from_idx, from_key_ring= from_node
    from_r, from_c = from_idx

    parent[to_r][to_c][to_key_ring] = from_node
    #print(to_r, to_c, to_key_ring, parent[to_r][to_c][to_key_ring])

    state[to_r][to_c][to_key_ring] = state[from_r][from_c][from_key_ring] + 1
    #print(state[to_r][to_c][to_key_ring])
    #print(to_r, to_c, to_key_ring, state[to_r][to_c][to_key_ring])
    visited[to_r][to_c][to_key_ring] = True
    q.append(((to_r, to_c), to_key_ring))

def bfs(grid, start, state, parent, visited):
    r, c = len(grid), len(grid[0])

    q = [] # stores ((r, c), key_ring)
    q.append((start, 0))
    sr, sc = start
    state[sr][sc][0] = 0
    visited[sr][sc][0] = True

    while q:
        start, st_key_ring = q.pop(0)
        sr, sc = start

        #print(sr, sc, st_key_ring)
        if is_stop(grid[sr][sc]):
            continue
            # not quitting to find all the paths

        for nr, nc in get_nbrs(sr, sc, grid):
            #nr = dr + sr
            #nc = dc + sc
            ch = grid[nr][nc]

            if is_water(ch):
                continue
            elif is_land(ch) or is_start(ch) or is_stop(ch):
                if visited[nr][nc][st_key_ring] == False:
                    add_nbr_to_q(nr, nc, st_key_ring, ((sr, sc), st_key_ring),
                            parent, state, visited, q)
            elif is_door(ch):
                if can_open_door(ch, st_key_ring):
                    if visited[nr][nc][st_key_ring] == False:
                        add_nbr_to_q(nr, nc, st_key_ring,
                                ((sr, sc), st_key_ring),
                                parent, state, visited, q)
            elif is_key(ch):
                new_key_ring = st_key_ring | (1 << (ord(ch) - ord('a')))
                if visited[nr][nc][new_key_ring] == False:
                    add_nbr_to_q(nr, nc, new_key_ring,
                            ((sr, sc), st_key_ring),
                            parent, state, visited, q)

def get_nbrs(sr, sc, grid):
    r, c = len(grid), len(grid[0])
    move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    output = []

    for dr, dc in move:
        nr = sr + dr
        nc = sc + dc

        if 0<= nr < r and 0<= nc < c:
            output.append((nr, nc))

    return output


def build_path(state, parent, key_ring, st, end):
    ans = []
    er, ec = end
    ans.append(end)

    #print(key_ring, st, end)
    while end != st or key_ring != 0:
        par = parent[er][ec][key_ring]
        #print(par)
        end, key_ring = par
        er, ec = end
        ans.append(end)

    #print(ans)
    return ans[::-1]

def get_start_end_cell(grid):
    r, c = len(grid), len(grid[0])

    start, end = None, None

    for i in range(r):
        for j in range(c):
            ch = grid[i][j]

            if is_start(ch):
                start = (i, j)

            if is_stop(ch):
                end = (i, j)

            if start and end:
                return start, end

    return start, end

grid = [
        ['.', '.', '.', 'B'],
        ['.', 'b', '#', '.'],
        ['@', '#', '+', '.']
       ]
for i in range(len(grid)):
    print(grid[i])
print()
print("Shortest path:", shortest_path(grid))

