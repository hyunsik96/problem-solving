import sys
from heapq import heappop, heappush

input = sys.stdin.readline

pq = []

N = int(input())

nums = map(int, input().split())

for num in nums:
    heappush(pq, num)

for _ in range(N - 1):
    nums = map(int, input().split())
    for num in nums:
        if num > pq[0]:
            heappop(pq)
            heappush(pq, num)

print(heappop(pq))
