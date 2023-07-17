import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())

graph = [[True]*m for _ in range(n)]

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for x in range(lx, rx):
        for y in range(ly, ry):
            if graph[x][y]:
                graph[x][y] = False

ans = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(x, y):
    area = 1
    graph[x][y] = False
    deq = deque([(x, y)])
    while deq:
        tmp = deq.popleft()
        for i in range(4):
            nx, ny = tmp[0] + dx[i], tmp[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                deq.append((nx, ny))
                graph[nx][ny] = False
                area += 1
    return area

for x in range(n):
    for y in range(m):
        if graph[x][y]:
            ans.append(bfs(x, y))

print(len(ans))
print(*(sorted(ans)))
