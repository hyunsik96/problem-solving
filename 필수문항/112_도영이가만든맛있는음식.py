import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
foods = []
for _ in range(N):
    foods.append(list(map(int, input().split())))
ans_gap = float("inf")
for i in range(1, N + 1):
    for comb_set in combinations(foods, i):
        s = 1
        b = 0
        for x, y in comb_set:
            s *= x
            b += y
        if ans_gap > abs(s - b):
            ans_gap = abs(s - b)

print(ans_gap)
