import sys
from collections import deque

que = deque([])

input = sys.stdin.readline

m, n, h = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# graph[h][n][m]

for z in range(h):
    for y in range(n):
        for x in range(m):
            num = graph[z][y][x]
            if num >= 1:
                que.append((x, y, z, num))

dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]

while que:
    tmp_xyz = que.popleft()
    for i in range(6):
        next_x, next_y, next_z, next_num = tmp_xyz[0] + dx[i], tmp_xyz[1] + dy[i], tmp_xyz[2] + dz[i], tmp_xyz[3] + 1
        if 0 <= next_x < m and 0 <= next_y < n and 0 <= next_z < h and graph[next_z][next_y][next_x] == 0:
            graph[next_z][next_y][next_x] = next_num
            que.append((next_x, next_y, next_z, next_num))

ans = 0

for z in range(h):
    for y in range(n):
        for x in range(m):
            num = graph[z][y][x]
            if num == 0:
                print(-1)
                exit()
            ans = max(ans, num)

print(ans-1)