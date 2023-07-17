import sys

input = sys.stdin.readline

n = int(input())

grape = [0]*n

for i in range(n):
    grape[i] = int(input())

dp1 = [0]*n
dp2 = [0]*n
dp3 = [0]*n

dp2[0] = grape[0]
dp3[0] = grape[0]

for i in range(1, n):
    dp1[i] = max(dp1[i-1], dp2[i-1], dp3[i-1])
    dp2[i] = dp1[i-1] + grape[i]
    dp3[i] = dp2[i-1] + grape[i]

print(max(dp1[n-1], dp2[n-1], dp3[n-1]))