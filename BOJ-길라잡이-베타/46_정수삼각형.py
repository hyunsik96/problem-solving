import sys

input = sys.stdin.readline

n = int(input())

dp = [[0]*(i+1) for i in range(n)]

dp[0][0] = int(input())

for i in range(1, n):
    idx = 0
    for x in list(map(int, input().split())):
        if idx == 0:
            dp[i][0] = dp[i-1][0] + x
        elif idx == i:
            dp[i][idx] = dp[i-1][i-1] + x
        else:
            dp[i][idx] = max(dp[i-1][idx-1], dp[i-1][idx]) + x
        idx += 1

print(max(dp[n-1]))