import sys
from decimal import Decimal

input = sys.stdin.readline

N = int(input())
nums = [Decimal(input()) for _ in range(N)]

dp = [Decimal(0)] * N
dp[0] = nums[0]
for i in range(1, N):
    if dp[i - 1] * nums[i] > nums[i]:
        dp[i] = dp[i - 1] * nums[i]
    else:
        dp[i] = nums[i]
print(round(max(dp), 3))
