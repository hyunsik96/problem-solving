import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]

dp = [[0] * (N + 1) for _ in range(N + 1)]

for con in graph:
    dp[con[0]][con[1]] = 1
    dp[con[1]][con[0]] = 1


for start in range(1, N + 1):  # 1부터 N까지 하나씩(i) 연결관계 정립
    check = [True] * (N + 1)
    check[start] = False
    deq = deque([start])

    while deq:
        mid = deq.popleft()

        for end in range(1, N + 1):
            if check[end] and dp[mid][end] == 1:
                check[end] = False
                deq.append(end)
                if dp[start][end] == 0:
                    dp[start][end] = dp[start][mid] + dp[mid][end]
                else:
                    dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid][end])

ans = 0
ans_sum = N * (N + 1)

for i in range(1, N + 1):
    sum_dp = sum(dp[i])
    if sum_dp < ans_sum:
        ans = i
        ans_sum = sum_dp

print(ans)
