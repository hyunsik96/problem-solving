import sys
import heapq

n = int(sys.stdin.readline())
pq = []
ans_list = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if pq: ans_list.append(heapq.heappop(pq))
        else: ans_list.append(0)
    else:
        heapq.heappush(pq, -1*x)

for k in ans_list:
    print(-1*k)