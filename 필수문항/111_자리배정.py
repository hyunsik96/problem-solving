import sys

input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
else:
    graph = [[0, 0] for _ in range(C * R + 1)]
    graph[0][0] = 1
    wall = [R, C, 1, 1]  # top, right, down, left
    pointer = 0

    for num in range(1, C * R + 1):
        if pointer == 0:
            x, y = graph[num - 1]
            graph[num][0] = x
            graph[num][1] = y + 1
            if graph[num][1] == wall[pointer]:
                pointer = 1
                wall[3] += 1
        elif pointer == 1:
            x, y = graph[num - 1]
            graph[num][1] = y
            graph[num][0] = x + 1
            if graph[num][0] == wall[pointer]:
                pointer = 2
                wall[0] -= 1
        elif pointer == 2:
            x, y = graph[num - 1]
            graph[num][0] = x
            graph[num][1] = y - 1
            if graph[num][1] == wall[pointer]:
                pointer = 3
                wall[1] -= 1
        else:
            x, y = graph[num - 1]
            graph[num][1] = y
            graph[num][0] = x - 1
            if graph[num][0] == wall[pointer]:
                pointer = 0
                wall[2] += 1

    print(*graph[K], sep=" ")
