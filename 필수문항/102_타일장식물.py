import sys

input = sys.stdin.readline

N = int(input())

x, y = 1, 1

for i in range(2, N + 1):
    x = x + y
    y = x - y

print((x + y) * 2)
