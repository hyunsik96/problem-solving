import sys
import math

input = sys.stdin.readline

N, K, I = map(int, input().split())
peak = N // 2 + 1

i = 0
while i < peak:
    K = math.ceil(K / 2)
    I = math.ceil(I / 2)
    i += 1
    if K == I:
        print(i)
        break
