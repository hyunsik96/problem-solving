import sys

input = sys.stdin.readline

N, _ = map(int, input().split())
line = [[] for _ in range(7)]
ans = 0

for _ in range(N):
    l, p = map(int, input().split())
    while line[l] and line[l][-1] > p:
        line[l].pop()
        ans += 1
    if not line[l] or line[l][-1] != p:
        line[l].append(p)
        ans += 1

print(ans)
