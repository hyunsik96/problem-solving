import sys
from heapq import heappop, heappush

input = sys.stdin.readline
N, M = map(int, input().split())

cards = []
for num in map(int, input().split()):
    heappush(cards, num)

ans = sum(cards)

for _ in range(M):
    a = heappop(cards)
    b = heappop(cards)
    ans += a + b
    heappush(cards, a + b)
    heappush(cards, a + b)

print(ans)
