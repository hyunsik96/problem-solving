import sys
import math

input = sys.stdin.readline

N, M, K = map(int, input().split())

dp = [1] * 31
for i in range(1, 31):
    dp[i] = dp[i - 1] * i

x = (K - 1) // M
y = K - x * M - 1
if K == 0:
    x = 0
    y = 0
# (0, 0) -> (x, y) -> (N-1, M-1)
print(
    int(
        (dp[x + y] / dp[x] / dp[y])
        * (dp[N + M - 2 - x - y] / dp[N - 1 - x] / dp[M - 1 - y])
    )
)
