import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

bfs_queue = deque([n])
ans = [-1]*150001
ans[n] = 0

while bfs_queue:
    x = bfs_queue.popleft()
    if x == k:
        print(ans[x])
        exit()
    for t in [x+1, x-1, 2*x]:
        if 0 <= t <= 150000 and ans[t] == -1:
            bfs_queue.append(t)
            ans[t] = ans[x] + 1


# ans_list = deque([[n, 0]])  # 메모리초과

# while ans_list:
#     tmp = ans_list.popleft()
#     x = tmp[0]
#     y = tmp[1]
#     if x+1 == k or x-1 == k or x*2 == k:
#         print(y+1)
#         exit()
#     ans_list.append([x+1, y+1])
#     ans_list.append([x-1, y+1])
#     ans_list.append([2 * x, y+1])