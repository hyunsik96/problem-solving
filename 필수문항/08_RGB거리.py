import sys

input = sys.stdin.readline

n = int(input())

price = list(map(int, input().split()))

for i in range(1, n):
    r, g, b = map(int, input().split())
    r = min(price[1], price[2]) + r
    g = min(price[0], price[2]) + g
    b = min(price[0], price[1]) + b
    price[0] = r
    price[1] = g
    price[2] = b

print(min(price))
