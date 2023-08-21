import sys
from collections import deque

input = sys.stdin.readline

N = int(input())


def check_point(x, y, count, l):
    if 0 <= x < l and 0 <= y < l and graph[x][y]:
        deq.append([x, y, count + 1, l])
        graph[x][y] = False


for _ in range(N):
    L = int(input())
    from_x, from_y = map(int, input().split())
    to_x, to_y = map(int, input().split())
    graph = [[True] * L for _ in range(L)]
    graph[from_x][from_y] = False
    deq = deque([[from_x, from_y, 0]])

    while deq:
        origin = deq.popleft()
        if origin[0] == to_x and origin[1] == to_y:
            print(origin[2])
            break
        check_point(origin[0] + 2, origin[1] + 1, origin[2], L)
        check_point(origin[0] + 2, origin[1] - 1, origin[2], L)
        check_point(origin[0] - 2, origin[1] + 1, origin[2], L)
        check_point(origin[0] - 2, origin[1] - 1, origin[2], L)
        check_point(origin[0] + 1, origin[1] + 2, origin[2], L)
        check_point(origin[0] + 1, origin[1] - 2, origin[2], L)
        check_point(origin[0] - 1, origin[1] + 2, origin[2], L)
        check_point(origin[0] - 1, origin[1] - 2, origin[2], L)
