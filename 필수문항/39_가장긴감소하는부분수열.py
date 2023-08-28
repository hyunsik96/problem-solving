import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    max_num, max_count = 0, 0
    for idx in range(i):
        if A[idx] > A[i] and dp[idx] > max_count:
            max_num, max_count = A[idx], dp[idx]
    dp[i] = max_count + 1

print(max(dp))
