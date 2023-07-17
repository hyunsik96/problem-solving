import sys

input = sys.stdin.readline

n = int(input())

p = [0] + list(map(int, input().split()))

dp = [0]*(n+1)

dp[1] = p[1]

for i in range(1, n+1):
    dp[i] = max(p[i-x] + dp[x] for x in range(i))

print(dp[n])