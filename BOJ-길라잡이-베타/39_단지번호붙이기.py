import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, list(input().strip()))) for _ in range(n)]

check = [[False]*n for _ in range(n)]

def bfs(x, y):
    ans = 0
    tmp_que = deque([])
    if graph[x][y] == 1 and check[x][y] == False:
        tmp_que.append([x, y])
        check[x][y] = True
        ans += 1
    
    while tmp_que:
        tmp_xy = tmp_que.popleft()
        tmp_x, tmp_y = tmp_xy[0], tmp_xy[1]

        if tmp_x != 0 and graph[tmp_x - 1][tmp_y] == 1 and check[tmp_x - 1][tmp_y] == False:
            tmp_que.append([tmp_x - 1, tmp_y])
            check[tmp_x - 1][tmp_y] = True
            ans += 1

        if tmp_y != 0 and graph[tmp_x][tmp_y - 1] == 1 and check[tmp_x][tmp_y - 1] == False:
            tmp_que.append([tmp_x, tmp_y - 1])
            check[tmp_x][tmp_y - 1] = True
            ans += 1

        if tmp_x != n-1 and graph[tmp_x + 1][tmp_y] == 1 and check[tmp_x + 1][tmp_y] == False:
            tmp_que.append([tmp_x + 1, tmp_y])
            check[tmp_x + 1][tmp_y] = True
            ans += 1

        if tmp_y != n-1 and graph[tmp_x][tmp_y + 1] == 1 and check[tmp_x][tmp_y + 1] == False:
            tmp_que.append([tmp_x, tmp_y + 1])
            check[tmp_x][tmp_y + 1] = True
            ans += 1

    return ans

ans_list = []

for x in range(n):
    for y in range(n):
        if check[x][y] == False and graph[x][y] == 1:
            ans_list.append(bfs(x, y))

print(len(ans_list))
for x in sorted(ans_list):
    print(x)