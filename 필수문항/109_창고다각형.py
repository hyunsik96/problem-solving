import sys

input = sys.stdin.readline

N = int(input())
graph = [0] * 1001
tall = 0

for _ in range(N):
    L, H = map(int, input().split())
    graph[L] = H
    tall = max(tall, H)

lp = 1
rp = 1000

ls = 1
rs = 1000
lh = graph[1]
rh = graph[1000]
ans = 0

while graph[lp] != tall:
    if graph[lp] > lh:
        ans += (lp - ls) * lh
        lh = graph[lp]
        ls = lp
    lp += 1
ans += (lp - ls) * lh

while graph[rp] != tall:
    if graph[rp] > rh:
        ans += (rs - rp) * rh
        rh = graph[rp]
        rs = rp
    rp -= 1
ans += (rs - rp) * rh

ans += (rp - lp + 1) * tall

print(ans)
