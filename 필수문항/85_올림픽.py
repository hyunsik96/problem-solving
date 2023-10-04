import sys

input = sys.stdin.readline

N, K = map(int, input().split())

medal = [list(map(int, input().split())) for _ in range(N)]

medal.sort(key=lambda x: [x[1], x[2], x[3]])
rank = 0
for i in range(N):
    if medal[i][0] == K:
        rank = i
        break

while rank < N - 1 and medal[rank][1:] == medal[rank + 1][1:]:
    rank += 1

print(N - rank)
