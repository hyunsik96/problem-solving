import sys
from collections import deque

input = sys.stdin.readline

# F: 총 층수, S: 현재 층, G: 목적지 층, U: 위로 올라가는 층 수, D: 아래로 내려가는 층 수
F, S, G, U, D = map(int, input().split())

bfs = deque([[S, 0]])
check = [False] * (F + 1)

while bfs:
    floor, count = bfs.popleft()
    if floor == G:
        print(count)
        exit()

    if floor + U <= F and not check[floor + U]:
        bfs.append([floor + U, count + 1])
        check[floor + U] = True
    if floor - D >= 1 and not check[floor - D]:
        bfs.append([floor - D, count + 1])
        check[floor - D] = True

print("use the stairs")
