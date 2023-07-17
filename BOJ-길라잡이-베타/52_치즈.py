# import sys    # 시간초과 ..
# from collections import deque

# input = sys.stdin.readline

# x, y = map(int, input().split())

# graph = [list(map(int, input().split())) for _ in range(x)]
# one = []
# ans = 0

# dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# deq = deque([(0, 0)])

# while deq:
#     tmp = deq.popleft()
#     graph[tmp[0]][tmp[1]] = 2
#     for i in range(4):
#         nx, ny = dx[i] + tmp[0], dy[i] + tmp[1]
#         if 0 <= nx < x and 0 <= ny < y and graph[nx][ny] == 0:
#             deq.append((nx, ny))

# for m in range(x):
#     for n in range(y):
#         if graph[m][n] == 1:
#             one.append([m, n, True])

# check_num = len(one)

# def change(num):
#     global check_num
#     tmp_num = 0
#     tmp_arr = []
#     for o in one:
#         if o[2]:
#             for i in range(4):
#                 nx, ny = dx[i] + o[0], dy[i] + o[1]
#                 if 0 <= nx < x and 0 <= ny < y and graph[nx][ny] == num:
#                     o[2] = False
#                     tmp_arr.append((o[0], o[1]))
#                     check_num -= 1
#                     tmp_num += 1
#                     break
#     for z in tmp_arr:
#         graph[z[0]][z[1]] = num
#     return tmp_num

# def hole(num):
#     while deq:
#         tmp = deq.popleft()
#         graph[tmp[0]][tmp[1]] = num + 1
#         for i in range(4):
#             nx, ny = dx[i] + tmp[0], dy[i] + tmp[1]
#             if 0 <= nx < x and 0 <= ny < y and (graph[nx][ny] == num or graph[nx][ny] == 0):
#                 deq.append((nx, ny))

# ans2 = 0
# while check_num:
#     ans += 1
#     ans2 = 0
#     ans2 = change(ans + 1)
#     deq = deque([(0, 0)])
#     hole(ans + 1)

# print(ans)
# print(ans2)

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs():
    q = deque([(0, 0)])
    melt = deque([])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if cheeze[nx][ny] == 0:  # 공기면 계속 탐색하기 위해 큐에 넣음
                    q.append((nx, ny))
                elif cheeze[nx][ny] == 1:  # 치즈면 한 번에 녹이기 위해 melt에 넣음
                    melt.append((nx, ny))
                    
    for x, y in melt:
        cheeze[x][y] = 0  # 공기와 닿은 치즈를 한 번에 녹임
    return len(melt)  # 녹인 치즈 갯수 리턴

n, m = map(int, input().split())
cheeze = []
cnt = 0
for i in range(n):
    cheeze.append(list(map(int, input().split())))
    cnt += sum(cheeze[i])  # 전체 치즈 갯수 카운트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while True:
    visited = [[0] * m for _ in range(n)]
    meltCnt = bfs()
    cnt -= meltCnt
    if cnt == 0:  # 치즈를 다 녹였으면
        print(time, meltCnt, sep='\n')  # 시간과 직전에 녹인 치즈 갯수를 출력
        break
    time += 1