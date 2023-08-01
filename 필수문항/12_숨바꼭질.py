import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

bfs_queue = deque([n])
ans = [-1] * 150001
ans[n] = 0

while bfs_queue:
    x = bfs_queue.popleft()
    if x == k:
        print(ans[x])
        exit()
    for t in [x + 1, x - 1, 2 * x]:
        if 0 <= t <= 150000 and ans[t] == -1:
            bfs_queue.append(t)
            ans[t] = ans[x] + 1
