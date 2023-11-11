import sys

input = sys.stdin.readline
R, C, N = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
if N == 1:
    for s in graph:
        print(*s, sep="")
elif N % 2 == 0:
    for _ in range(R):
        print("O" * C)

else:
    N //= 2
    bomb = set()

    for x in range(R):
        for y in range(C):
            if graph[x][y] == "O":
                bomb.add((x, y))

    for _ in range(N):
        new_bomb = set()
        for x, y in bomb:
            new_bomb.add((x, y))
            for i in range(4):
                if 0 <= x + dx[i] < R and 0 <= y + dy[i] < C:
                    new_bomb.add((x + dx[i], y + dy[i]))
        bomb = set()
        for x in range(R):
            for y in range(C):
                if (x, y) not in new_bomb:
                    bomb.add((x, y))
    graph = [["."] * C for _ in range(R)]
    for x, y in bomb:
        graph[x][y] = "O"
    for s in graph:
        print(*s, sep="")
