import sys
import math

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    print(math.comb(10 + n - 1, n))
