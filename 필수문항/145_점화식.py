import sys

input = sys.stdin.readline

dp = [0] * 36
dp[0] = 1
for i in range(1, 36):
    for l in range(i):
        dp[i] += dp[l] * dp[i - l - 1]

print(dp[int(input())])
