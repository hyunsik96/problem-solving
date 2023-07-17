import sys

input = sys.stdin.readline

n = int(input())

budget = list(map(int, input().split()))

total = int(input())

pl = 1
pr = max(budget)
ans = 0

# 이분탐색시 확인할 부분
def check(m):
    tmp = 0
    for x in budget:
        if x > m:
            tmp += m
        else:
            tmp += x
    return tmp

while True:
    pc = (pl + pr) // 2
    if check(pc) <= total:
        ans = max(ans, pc)
        pl = pc + 1
    else:
        pr = pc - 1
    if pl > pr:
        break

print(ans)