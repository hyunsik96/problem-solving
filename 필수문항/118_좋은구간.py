import sys
from bisect import bisect_left

input = sys.stdin.readline

L = int(input())
good = sorted(list(map(int, input().split())))
n = int(input())

idx = bisect_left(good, n)
if good[idx] == n:
    print(0)
else:
    lp = good[idx - 1]
    if idx == 0:
        lp = 0
    rp = good[idx]
    print((n - lp) * (rp - n) - 1)
