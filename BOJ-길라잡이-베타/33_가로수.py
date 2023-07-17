import sys
import math

input = sys.stdin.readline

n = int(input())

tree = [int(input()) for i in range(n)]
gap = []
for i in range(0, len(tree)-1):
    gap.append(tree[i+1] - tree[i])

gcd = math.gcd(*gap)

ans = 0

for x in gap:
    ans += int(x / gcd) - 1

print(ans)