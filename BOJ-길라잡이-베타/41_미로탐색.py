import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def check(a, b):
    global n, m
    able = []
    if a > 0 and graph[a-1][b] == 1 and visited[a-1][b] == 0: able.append((a-1, b))
    if b > 0 and graph[a][b-1] == 1 and visited[a][b-1] == 0: able.append((a, b-1))
    if a < (n-1) and graph[a+1][b] == 1 and visited[a+1][b] == 0: able.append((a+1, b))
    if b < (m-1) and graph[a][b+1] == 1 and visited[a][b+1] == 0: able.append((a, b+1))
    return able

queue = deque([(0,0)])
visited[0][0] = 1

while queue:
    x, y = queue.popleft()

    if x == n-1 and y == m-1:
        print(visited[x][y])
        break
    
    for k in check(x, y):
        visited[k[0]][k[1]] = visited[x][y] + 1
        queue.append(k)