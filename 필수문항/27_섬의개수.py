import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

while True:
    w, h = map(int, input().split())
    ans = 0
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    que = deque([])

    for x in range(w):
        for y in range(h):
            if graph[y][x] == 1:
                ans += 1
                que.append([y, x])
                graph[y][x] = 0
            while que:
                pop_land = que.popleft()
                for i in range(8):
                    if (
                        0 <= pop_land[1] + dx[i] < w
                        and 0 <= pop_land[0] + dy[i] < h
                        and graph[pop_land[0] + dy[i]][pop_land[1] + dx[i]] == 1
                    ):
                        que.append([pop_land[0] + dy[i], pop_land[1] + dx[i]])
                        graph[pop_land[0] + dy[i]][pop_land[1] + dx[i]] = 0
    print(ans)
