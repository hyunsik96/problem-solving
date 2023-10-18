import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
o, v = 0, 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for x in range(R):
    for y in range(C):
        if graph[x][y] != "#" and not visited[x][y]:
            deq = deque([(x, y)])
            visited[x][y] = True
            no, nv = 0, 0
            while deq:
                nx, ny = deq.popleft()
                if graph[nx][ny] == "o":
                    no += 1
                elif graph[nx][ny] == "v":
                    nv += 1
                for i in range(4):
                    if (
                        0 <= nx + dx[i] < R
                        and 0 <= ny + dy[i] < C
                        and graph[nx + dx[i]][ny + dy[i]] != "#"
                        and not visited[nx + dx[i]][ny + dy[i]]
                    ):
                        deq.append((nx + dx[i], ny + dy[i]))
                        visited[nx + dx[i]][ny + dy[i]] = True
            if no > nv:
                o += no
            else:
                v += nv
print(o, v)
