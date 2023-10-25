import sys

input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(19)]
direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1)]


def valid(x, y, num):
    global graph
    return 0 <= x < 19 and 0 <= y < 19 and graph[x][y] == num


def check(x, y, dx, dy):
    global graph
    count = 1
    num = graph[x][y]
    while valid(x + dx, y + dy, num):
        x += dx
        y += dy
        count += 1
    return count


for x in range(19):
    for y in range(19):
        if graph[x][y] != 0:
            for dx, dy in direction:
                count = 1

                if valid(x + dx, y + dy, graph[x][y]):
                    count += check(x + dx, y + dy, dx, dy)

                if valid(x - dx, y - dy, graph[x][y]):
                    count += check(x - dx, y - dy, -dx, -dy)

                if count == 5:
                    if dy == 1:
                        dx = -dx
                        dy = -dy
                    elif dy == 0 and dx == 1:
                        dx = -dx
                    num = graph[x][y]
                    while valid(x + dx, y + dy, num):
                        x += dx
                        y += dy
                    print(num)
                    print(x + 1, y + 1)
                    exit()

print(0)
