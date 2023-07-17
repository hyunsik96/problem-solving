import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

cards = []

for _ in range(n):
    heappush(cards, int(input()))

ans = 0

# 작은순서대로 꺼내고 합치는데 필요한 합을 정답에 더해준다.
# 합치는데 사용한 두 묶음은 pop됐고, 합쳐진 묶음은 새로 힙에 넣어준다.
while len(cards) > 1:
    card1 = heappop(cards)
    card2 = heappop(cards)
    ans += card1 + card2
    heappush(cards, card1 + card2)

print(ans)