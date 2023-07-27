import sys

input = sys.stdin.readline

n = int(input())

stair = [int(input()) for _ in range(n)]

dp = [[0, 0], [stair[0], stair[0]]]

for i in range(1, n):
    dp.append([dp[i][1] + stair[i], max(dp[i - 1]) + stair[i]])

print(max(dp[n]))
