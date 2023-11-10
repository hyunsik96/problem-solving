import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())
moneys = [int(input()) for _ in range(N)]
sum_moneys = sum(moneys)
lp = max(max(moneys), math.ceil(sum_moneys / M))
rp = sum_moneys

while lp <= rp:
    mid = (lp + rp) // 2
    tmp_sum = 0
    tmp_ans = 1
    for money in moneys:
        if tmp_sum + money > mid:
            tmp_ans += 1
            tmp_sum = money
        else:
            tmp_sum += money
    if tmp_ans > M:
        lp = mid + 1
    else:
        rp = mid - 1

print(lp)
