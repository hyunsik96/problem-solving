import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))

dp = [0]*n

dp[0] = num_list[0]

for i in range(1, n):
    if dp[i-1] > 0:
        dp[i] = dp[i-1] + num_list[i]
    else:
        dp[i] = num_list[i]

print(max(dp))