#!/usr/bin/env python3

def edit_distance(s1, s2):
    l1, l2 = len(s1), len(s2)

    res = [[ float('inf') for _ in range(l2+1)]
            for _ in range(l1+1)]

    for i in range(l1, -1, -1):
        for j in range(l2, -1, -1):

            if i == l1 and j == l2:
                res[i][j] = 0
            elif i == l1:
                res[i][j] = l2 - j
            elif j == l2:
                res[i][j] = l1 - i
            elif s1[i] == s2[j]:
                res[i][j] = res[i+1][j+1]
            else:
                res[i][j] = min(res[i+1][j], res[i][j+1], res[i+1][j+1]) + 1

    for i in range(l1+1):
        print(res[i])
    return(res[0][0])

s1 = "anmation"
s2 = "animesh"
print(edit_distance(s1, s2))

