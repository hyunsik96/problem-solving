import sys

input = sys.stdin.readline

n, m = map(int, input().split())

tree = list(map(int, input().split()))

def check(h):
    total = 0
    for x in tree:
        if x > h:
            total += x-h
    return total

pl = 0
pr = max(tree)
ans = -1

while True:
    pc = (pl + pr) // 2
    if check(pc) >= m:
        ans = max(ans, pc)
        pl = pc + 1
    else:
        pr = pc - 1
    
    if pl > pr:
        break

print(ans)