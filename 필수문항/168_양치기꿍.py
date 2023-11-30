import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [input().rstrip() for _ in range(R)]
visited = [[False] * C for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
check = dict()
k = 0
v = 0

for x in range(R):
    for y in range(C):
        if not visited[x][y] and graph[x][y] != "#":
            que = deque()
            que.append((x, y))
            visited[x][y] = True
            check["k"] = 0
            check["v"] = 0
            if graph[x][y] != ".":
                check[graph[x][y]] += 1
            while que:
                nx, ny = que.popleft()
                for i in range(4):
                    if (
                        0 <= nx + dx[i] < R
                        and 0 <= ny + dy[i] < C
                        and graph[nx + dx[i]][ny + dy[i]] != "#"
                        and not visited[nx + dx[i]][ny + dy[i]]
                    ):
                        visited[nx + dx[i]][ny + dy[i]] = True
                        if graph[nx + dx[i]][ny + dy[i]] != ".":
                            check[graph[nx + dx[i]][ny + dy[i]]] += 1
                        que.append((nx + dx[i], ny + dy[i]))
            if check["k"] > check["v"]:
                k += check["k"]
            else:
                v += check["v"]

print(k, v)
