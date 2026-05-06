#!/usr/bin/env python3

m = n = 8
visited = [ [ None for _ in range(m)] for _ in range(n) ]
visited[5][0] = (5, 0)
print(visited)
r, c = visited[5][0]
print("row:", r, ", col:", c)

output = []
output.append((1,2))
output.append((2,3))
print(output)

