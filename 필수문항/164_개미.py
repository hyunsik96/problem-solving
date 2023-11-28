import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    l, n = map(int, input().split())
    graph = [0] * n
    for i in range(n):
        graph[i] = int(input())
    graph.sort()
    if graph[0] == 0:
        graph.pop(0)
        n -= 1
        if not graph:
            print(0, 0)
            exit()
    if graph[-1] == l:
        graph.pop()
        n -= 1
        if not graph:
            print(0, 0)
            exit()
    min_ans = min(graph[0], l - graph[0])
    max_ans = graph[0]
    for i in range(1, n):
        min_ans = max(min_ans, min(l - graph[i], graph[i]))
        max_ans += graph[i] - graph[i - 1]
    max_ans += l - graph[-1]
    max_ans -= min(graph[0], l - graph[-1])
    print(min_ans, max_ans)
