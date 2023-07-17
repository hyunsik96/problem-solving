import sys

input = sys.stdin.readline

n = int(input())

# dp 테이블은 1 idx부터 n idx까지
dp = [[0, 0, 0] for _ in range(n+1)]

for i in range(1, n+1):
    i_list = list(map(int, input().split()))
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + i_list[0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + i_list[1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + i_list[2]

print(min(dp[n]))
