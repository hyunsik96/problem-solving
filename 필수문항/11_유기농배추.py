import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(T):
    M, N, K = map(int, input().split())
    ans = 0
    jr = []

    for _ in range(K):
        x, y = map(int, input().split())
        jr.append([x, y, 0])

    for i in range(K):
        if jr[i][2] == 1:
            continue

        jr[i][2] = 1
        ans += 1
        bfs = deque([jr[i]])

        while bfs:
            tmp = bfs.popleft()
            for i in range(4):
                for idx in range(K):
                    if jr[idx] == [tmp[0] + dx[i], tmp[1] + dy[i], 0]:
                        jr[idx][2] = 1
                        bfs.append(jr[idx])

    print(ans)
