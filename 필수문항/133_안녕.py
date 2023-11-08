import sys

input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))
visited = [False] * N
ans = 0


def dfs(idx, pleasure, health):
    global visited, ans
    for i in range(idx + 1, N):
        if not visited[i] and L[i] < health:
            visited[i] = True
            dfs(i, pleasure + J[i], health - L[i])
            visited[i] = False
    ans = max(ans, pleasure)


dfs(-1, 0, 100)
print(ans)
