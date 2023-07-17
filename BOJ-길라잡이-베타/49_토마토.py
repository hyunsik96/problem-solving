import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

que = deque([])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            que.append([x, y])

while que:
    x, y = que.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            que.append([nx, ny])
ans = 0
for x in range(n):
    for y in range(m):
        xy = graph[x][y]
        if xy == 0:
            print(-1)
            exit()
        ans = max(xy, ans)

print(ans-1)