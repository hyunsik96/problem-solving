import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N, score, P = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort()

ans = N - bisect_right(scores, score) + 1

if N - bisect_left(scores, score) + 1 > P:
    print(-1)
else:
    print(N - bisect_right(scores, score) + 1)
