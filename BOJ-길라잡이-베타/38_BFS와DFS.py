import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[False]*(n+1) for x in range(n+1)]

for x in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

check_d = [False]*(n+1)
ans_d = []
check_b = [False]*(n+1)
ans_b = []

def dfs(node):
    check_d[node] = True
    ans_d.append(node)

    for i, x in enumerate(graph[node]):
        if x and not check_d[i]:
            dfs(i)

dfs(v)

bfs_queue = deque([])
bfs_queue.append(v)
check_b[v] = True

while bfs_queue:
    tmp = bfs_queue.popleft()
    ans_b.append(tmp)
    for i, x in enumerate(graph[tmp]):
        if x and not check_b[i]:
            bfs_queue.append(i)
            check_b[i] = True

print(*ans_d)
print(*ans_b)