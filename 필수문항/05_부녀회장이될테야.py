import sys

input = sys.stdin.readline

T = int(input())

test_case = [[0, 0, i] for i in range(T)]
max_n = 0

for i in range(T):
    test_case[i][0] = int(input())
    test_case[i][1] = int(input())
    if max_n < test_case[i][1]:
        max_n = test_case[i][1]

test_case.sort(reverse=True)

dp = [[0] * (max_n + 1) for _ in range(test_case[0][0] + 1)]

for i in range(max_n + 1):
    dp[0][i] = i
for i in range(test_case[0][0] + 1):
    dp[i][1] = 1


def fill_kn(k, n):
    if dp[k][n] != 0:
        return

    if dp[k][n - 1] == 0:
        fill_kn(k, n - 1)

    if dp[k - 1][n] == 0:
        fill_kn(k - 1, n)

    dp[k][n] = dp[k][n - 1] + dp[k - 1][n]


for k, n, _ in test_case:
    fill_kn(k, n)

test_case.sort(key=lambda x: x[2])

for k, n, _ in test_case:
    print(dp[k][n])
