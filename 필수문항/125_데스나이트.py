import sys
from collections import deque

input = sys.stdin.readline

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

N = int(input())
from_x, from_y, to_x, to_y = map(int, input().split())

visited = [[False] * N for _ in range(N)]
visited[from_x][from_y] = True
queue = deque([(from_x, from_y, 0)])

while queue:
    x, y, count = queue.popleft()
    for i in range(6):
        if (
            0 <= x + dx[i] < N
            and 0 <= y + dy[i] < N
            and not visited[x + dx[i]][y + dy[i]]
        ):
            if x + dx[i] == to_x and y + dy[i] == to_y:
                print(count + 1)
                exit()

            visited[x + dx[i]][y + dy[i]] = True
            queue.append((x + dx[i], y + dy[i], count + 1))

print(-1)
