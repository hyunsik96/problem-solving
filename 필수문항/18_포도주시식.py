import sys

input = sys.stdin.readline

n = int(input())

if n == 2:
    print(int(input()) + int(input()))
elif n == 1:
    print(int(input()))
else:
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0][1] = int(input())
    dp[1][0] = dp[0][1]
    dp[1][1] = int(input())
    dp[1][2] = dp[0][1] + dp[1][1]

    for i in range(2, n):
        new_cup = int(input())
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = dp[i - 1][0] + new_cup
        dp[i][2] = dp[i - 1][1] + new_cup

    print(max(dp[n - 1]))
