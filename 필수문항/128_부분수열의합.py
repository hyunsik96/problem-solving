import sys

input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
S.sort()

dp = set()

for num in S:
    tmp = []
    for d in dp:
        tmp.append(num + d)
    for t in tmp:
        dp.add(t)
    dp.add(num)

ans = 1
dp = sorted(list(dp))
for num in dp:
    if num == ans:
        ans += 1
    else:
        print(ans)
        exit()
print(ans)
