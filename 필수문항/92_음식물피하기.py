import sys
from collections import deque

sys.setrecursionlimit = sys.maxsize
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[False] * m for _ in range(n)]
ans = 0
tmp_ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    global graph, dx, dy, tmp_ans
    deq = deque([(a, b)])
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            if (
                0 <= x + dx[i] < n
                and 0 <= y + dy[i] < m
                and graph[x + dx[i]][y + dy[i]]
            ):
                tmp_ans += 1
                graph[x + dx[i]][y + dy[i]] = False
                deq.append((x + dx[i], y + dy[i]))


for _ in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = True

for x in range(n):
    for y in range(m):
        if graph[x][y]:
            tmp_ans += 1
            graph[x][y] = False
            bfs(x, y)
            ans = max(ans, tmp_ans)
            tmp_ans = 0

print(ans)
