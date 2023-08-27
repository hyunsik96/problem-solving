import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)
dp[1] = 1
zegobs = [x**2 for x in range(1, N + 1)]

for dp_num in range(2, N + 1):
    min_num = 10000000001
    for zegob in zegobs:
        if dp_num >= zegob:
            min_num = min(min_num, dp[dp_num - zegob] + 1)
        else:
            break
    dp[dp_num] = min_num

print(dp[N])
