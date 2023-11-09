import sys

input = sys.stdin.readline

N, M = map(int, input().split())
sharks = []

for x in range(N):
    tmp = list(map(int, input().split()))
    for y in range(M):
        if tmp[y] == 1:
            sharks.append((x, y))

ans = 0

for x in range(N):
    for y in range(M):
        pa = max(N, M) - 1
        for sx, sy in sharks:
            tx = abs(sx - x)
            ty = abs(sy - y)
            ta = 0
            ta += min(tx, ty)
            ta += max(tx, ty) - ta
            pa = min(pa, ta)
        ans = max(ans, pa)

print(ans)
