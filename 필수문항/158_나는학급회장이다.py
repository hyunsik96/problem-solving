import sys

input = sys.stdin.readline

n = int(input())

candidates = [[0] * 5 for _ in range(3)]
candidates[0][4] = 1
candidates[1][4] = 2
candidates[2][4] = 3

for _ in range(n):
    scores = tuple(map(int, input().split()))
    for i in range(3):
        candidates[i][0] += scores[i]
        candidates[i][4 - scores[i]] += 1

candidates.sort(reverse=True)

if candidates[0][:4] == candidates[1][:4]:
    print(0, candidates[0][0])
else:
    print(candidates[0][4], candidates[0][0])
