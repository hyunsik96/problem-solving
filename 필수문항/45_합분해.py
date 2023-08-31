import sys
import math

input = sys.stdin.readline

N, K = map(int, input().split())

print(math.comb(K + N - 1, N) % 1000000000)
