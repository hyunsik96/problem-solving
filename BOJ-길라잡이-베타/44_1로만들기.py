import sys

n = int(sys.stdin.readline())

dp = [0]*(10**6+1)

dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 3
dp[6] = 2

for x in range(7, 10**6+1):
    ans = 10**6
    if x % 3 == 0 and dp[int(x / 3)] < ans:
        ans = dp[int(x / 3)]
    if x % 2 == 0 and dp[int(x / 2)] < ans:
        ans = dp[int(x / 2)]
    if dp[x - 1] < ans:
        ans = dp[x - 1]
    dp[x] = ans + 1

print(dp[n])