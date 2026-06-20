#!/usr/bin/env python3

def snake_ladder(board_sz, moves_list):
    
    # makes moves 0 based. Incoming moves is 1 based
    moves = [0] * len(moves_list)
    for i in range(len(moves_list)):
        moves[i] = moves_list[i]
        if moves[i] != -1:
            moves[i] -= 1

    return _snake_ladder(board_sz, moves)

def _snake_ladder(n, moves):
    visited = set()
    q = []
    dist = 0
    q.append( (0, dist))
    back_refs = {0:None}

    while q:
        cur, dist = q.pop(0)

        if cur in visited:
            continue

        if cur == n-1:
            #while cur:
            #    print(cur)
            #    cur = back_refs[cur]
            #print(back_refs)
            # If we need to print the dices used to reach the final
            # cell, I am kind of stuck here.
            return dist

        visited.add(cur)

        for dice in range(1,7):
            if cur + dice < n:
                if moves[cur+dice] == -1:
                    nxt = cur+dice
                else:
                    nxt = moves[cur+dice]

                q.append((nxt, dist+1))
                back_refs[nxt] = dice
                #print(back_refs)

    return -1 # can't reach final cell using the moves

n = 20
moves = [-1, -1, -1, -1, -1, -1, -1, -1, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
print("number of moves:", snake_ladder(n, moves))

