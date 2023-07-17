# import sys            # 시간초과

# sys.setrecursionlimit(1000000000)

# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = []
# check = [[True]*m for _ in range(n)]
# check[0][0] = False
# ans = 2000000

# for i in range(n):
#     tmp = input().strip()
#     for l in range(m):
#         if tmp[l] == '1':
#             graph.append((i, l))

# def dfs(x, y, cnt):
#     global ans
#     if x == n-1 and y == m-1:
#         ans = min(ans, cnt)
#         return

#     if x - 1 >= 0 and check[x-1][y] and (x-1, y) not in graph:
#         check[x-1][y] = False
#         dfs(x-1, y, cnt+1)
#         check[x-1][y] = True

#     if y - 1 >= 0 and check[x][y-1] and (x, y-1) not in graph:
#         check[x][y-1] = False
#         dfs(x, y-1, cnt+1)
#         check[x][y-1] = True

#     if x + 1 < n and check[x+1][y] and (x+1, y) not in graph:
#         check[x+1][y] = False
#         dfs(x+1, y, cnt+1)
#         check[x+1][y] = True

#     if y + 1 < m and check[x][y+1] and (x, y+1) not in graph:
#         check[x][y+1] = False
#         dfs(x, y+1, cnt+1)
#         check[x][y+1] = True


# for i in range(len(graph)):
#     tmp_pop = graph.pop(i)
#     dfs(0, 0, 1)
#     graph.insert(i, tmp_pop)

# if ans == 2000000:
#     print(-1)
# else:
#     print(ans)

from collections import deque

n, m = map(int, input().split())
graph = []

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and c == 0 :
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1


print(bfs(0, 0, 0))
