import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
ans = [[0] * N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            dp = []
            deq = deque([y])
            while deq:
                point = deq.popleft()
                ans[x][point] = 1
                if point == x or point in dp:
                    continue
                dp.append(point)
                for i in range(N):
                    if graph[point][i] == 1:
                        deq.append(i)

for row in ans:
    print(" ".join(map(str, row)))
