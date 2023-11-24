import sys

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for x in range(R):
    for y in range(C):
        if graph[x][y] == "S":
            for i in range(4):
                if 0 <= x + dx[i] < R and 0 <= y + dy[i] < C:
                    if graph[x + dx[i]][y + dy[i]] == "W":
                        print(0)
                        exit()
                    if graph[x + dx[i]][y + dy[i]] == ".":
                        graph[x + dx[i]][y + dy[i]] = "D"

print(1)
for i in range(R):
    print(*graph[i], sep="")
