import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

graph = [list(map(int, list(input().rstrip()))) for _ in range(M)]

queue = deque([])

for i in range(N):
    if graph[0][i] == 0:
        queue.append((0, i))
        graph[0][i] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        if (
            0 <= x + dx[i] < M
            and 0 <= y + dy[i] < N
            and graph[x + dx[i]][y + dy[i]] == 0
        ):
            if x + dx[i] == M - 1:
                print("YES")
                exit()
            queue.append((x + dx[i], y + dy[i]))
            graph[x + dx[i]][y + dy[i]] = 1

print("NO")
