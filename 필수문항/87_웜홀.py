import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M, W = map(int, input().split())
    graph = defaultdict(list)
    dist = [0] * (N + 1)

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((E, T))
        graph[E].append((S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((E, -T))

    for _ in range(N - 1):
        for s in range(1, N + 1):
            for e, t in graph[s]:
                dist[e] = min(dist[e], dist[s] + t)

    flag = False

    for s in range(1, N + 1):
        check = False
        for e, t in graph[s]:
            if dist[e] > (dist[s] + t):
                flag = True
                check = True
                break
        if check:
            break

    if flag:
        print("YES")
    else:
        print("NO")
