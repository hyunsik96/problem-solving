import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]

visited = [[False] * N for _ in range(M)]

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
ans = 0

for ox in range(M):
    for oy in range(N):
        if visited[ox][oy]:
            continue
        if graph[ox][oy] == 1:
            visited[ox][oy] = True
            ans += 1
            queue = deque()
            queue.append((ox, oy))
            while queue:
                x, y = queue.popleft()
                for i in range(8):
                    if (
                        0 <= x + dx[i] < M
                        and 0 <= y + dy[i] < N
                        and not visited[x + dx[i]][y + dy[i]]
                        and graph[x + dx[i]][y + dy[i]] == 1
                    ):
                        visited[x + dx[i]][y + dy[i]] = True
                        queue.append((x + dx[i], y + dy[i]))

print(ans)
