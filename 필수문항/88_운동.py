import sys

input = sys.stdin.readline

ans = float("inf")

V, E = map(int, input().split())
graph = [[float("inf")] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, V + 1):
    graph[k][k] = 0
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, V + 1):
    for b in range(a + 1, V + 1):
        ans = min(ans, graph[a][b] + graph[b][a])

print(-1) if ans == float("inf") else print(ans)
