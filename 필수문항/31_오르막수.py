import sys
import math

input = sys.stdin.readline

N = int(input())

print(math.comb(N + 9, 9) % 10007)
