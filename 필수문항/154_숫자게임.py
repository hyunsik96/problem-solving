import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

cards = [list(map(int, input().split())) for _ in range(n)]

ans = [0] * n

for i in range(n):
    for c in combinations(cards[i], 3):
        ans[i] = max(ans[i], sum(c) % 10)

answer = [-1, -1]
for i in range(n):
    if answer[0] <= ans[i]:
        answer[0] = ans[i]
        answer[1] = i
print(answer[1] + 1)
