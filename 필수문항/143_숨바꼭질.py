import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

d = [-1] * (N + 1)
d[1] = 0

que = deque([])

for place in graph[1]:
    d[place] = 1
    que.append((place, 1))

while que:
    place, distance = que.popleft()
    for p in graph[place]:
        if d[p] == -1:
            d[p] = distance + 1
            que.append((p, distance + 1))

ans = max(d)
print(d.index(ans), ans, d.count(ans))
