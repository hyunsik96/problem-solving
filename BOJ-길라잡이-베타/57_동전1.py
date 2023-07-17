# import sys # 시간초과

# input = sys.stdin.readline

# n, k = map(int, input().split())

# coin = [0]*n

# for i in range(n):
#     coin[i] = int(input())

# dp = [[] for _ in range(k+1)]

# idx = 0
# for x in coin:
#     if x <= k:
#         dp[x].append({m: 0 if m != x else 1 for m in coin})

# for i in range(k+1):
#     for x in coin:
#         if i - x > 0:
#             for y in dp[i-x]:
#                 tmp = y.copy()
#                 tmp[x] += 1
#                 if tmp not in dp[i]:
#                     dp[i].append(tmp)

# print(len(dp[k]))

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coin = [0]*n

for i in range(n):
    coin[i] = int(input())

dp = [0] * (k+1)
dp[0] = 1

for x in coin:
    for i in range(x, k+1):
        dp[i] += dp[i-x]

result = dp[k]
print(result)
