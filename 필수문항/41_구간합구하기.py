import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dp_graph = []

for _ in range(N):
    row = list(map(int, input().split()))
    dp_row = [0] * N
    dp_row[0] = row[0]
    for i in range(1, N):
        dp_row[i] = dp_row[i - 1] + row[i]
    dp_graph.append(dp_row)

for _ in range(M):
    Xa, Ya, Xb, Yb = map(int, input().split())
    ans = 0
    for row in range(Xa - 1, Xb):
        if Ya - 1 == 0:
            ans += dp_graph[row][Yb - 1]
        else:
            ans += dp_graph[row][Yb - 1] - dp_graph[row][Ya - 2]
    print(ans)
