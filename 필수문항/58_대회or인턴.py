import sys
import math

input = sys.stdin.readline

N, M, K = map(int, input().split())

team = 0

if N > 2 * M:
    team += M
    M = 0
    N -= 2 * team
    if N < K:
        team -= math.ceil((K - N) / 3)
else:
    team += N // 2
    N -= (N // 2) * 2
    M -= team
    if N + M < K:
        team -= math.ceil((K - N - M) / 3)

if team <= 0:
    print(0)
else:
    print(team)
