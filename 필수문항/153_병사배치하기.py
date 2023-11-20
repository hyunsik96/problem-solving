import sys

input = sys.stdin.readline
n = int(input())

s = list(map(int, input().split()))
s.append(0)
dp = [i for i in range(n + 1)]
for i in range(1, n + 1):
    for l in range(1, i + 1):
        if dp[i] > dp[i - l] + l - 1:
            if s[i - l] > s[i]:
                dp[i] = dp[i - l] + l - 1

print(dp[-1])
