import sys

input = sys.stdin.readline

N = int(input())

level = [0] * N

for i in range(N):
    level[i] = int(input())

ans = 0

for i in range(N - 2, -1, -1):
    if level[i + 1] <= level[i]:
        ans += level[i] - level[i + 1] + 1
        level[i] = level[i + 1] - 1

print(ans)
