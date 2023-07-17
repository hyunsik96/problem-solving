import sys

input = sys.stdin.readline

k, n = map(int, input().split())

rope = [int(input()) for _ in range(k)]

def check(h):
    total = 0
    for x in rope:
        total += x // h
    return total

pl = 1
pr = max(rope)
ans = 0

while True:
    pc = (pl + pr) // 2
    if check(pc) >= n:
        ans = max(ans, pc)
        pl = pc + 1
    else:
        pr = pc - 1
    if pl > pr:
        break

print(ans)