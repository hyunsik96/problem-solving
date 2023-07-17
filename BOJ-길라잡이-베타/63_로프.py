import sys

input = sys.stdin.readline

n = int(input())

lope = [0]*n
ans = 0

for i in range(n):
    lope[i] = int(input())

lope.sort()

for i in range(n):
    ans = max(ans, lope[i] * (n-i))

print(ans)