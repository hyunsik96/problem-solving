import sys

from heapq import heappop, heappush

input = sys.stdin.readline

que = []

n = int(input())

for _ in range(n):
    num = int(input())
    if num == 0 and len(que) == 0:
        print(0)
    elif num == 0 and len(que) != 0:
        print(heappop(que)[1])
    else:
        heappush(que, [abs(num), num])