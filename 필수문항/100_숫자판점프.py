import sys

input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(5)]
ans = set()


def check(x, y, jump, num, graph, ans):
    if jump == 5:
        ans.add(num)
        return
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        if 0 <= x + dx[i] < 5 and 0 <= y + dy[i] < 5:
            num += graph[x + dx[i]][y + dy[i]] * (10 ** (4 - jump))
            check(x + dx[i], y + dy[i], jump + 1, num, graph, ans)
            num -= graph[x + dx[i]][y + dy[i]] * (10 ** (4 - jump))


for x in range(5):
    for y in range(5):
        check(x, y, 0, graph[x][y] * 100000, graph, ans)

print(len(ans))
