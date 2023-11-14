import sys

input = sys.stdin.readline

n = int(input())

graph = [[False] * 102 for _ in range(102)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for l in range(10):
            graph[x + i + 1][y + l + 1] = True

ans = 0

for a in range(1, 102):
    for b in range(1, 102):
        # a,b ~ a+1,b => a,b & a, b-1 / a,b ~ a,b+1 => a,b & a-1,b
        if graph[a][b] != graph[a][b - 1]:
            ans += 1
        if graph[a][b] != graph[a - 1][b]:
            ans += 1
print(ans)
