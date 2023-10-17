import sys

dp = [0] * 41
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 41):
    dp[i] = dp[i - 1] + dp[i - 2]


input = sys.stdin.readline

N = int(input())
M = int(input())
ans = 1
last = 0
for _ in range(M):
    VIP = int(input())
    ans *= dp[VIP - last - 1]
    last = VIP

if last < N:
    ans *= dp[N - last]

print(ans)
