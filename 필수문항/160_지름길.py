import sys

input = sys.stdin.readline

N, D = map(int, input().split())

routes = []
for _ in range(N):
    a, b, price = map(int, input().split())
    if D < b or b - a - price <= 0:
        continue
    routes.append((a, b, b - a - price))
routes.sort()
N = len(routes)
ans = D


def dfs(idx, D):
    global routes, ans
    D -= routes[idx][2]
    check = False
    for i in range(idx + 1, N):
        if routes[idx][1] <= routes[i][0]:
            check = True
            dfs(i, D)
    if not check:
        ans = min(ans, D)


for i in range(N):
    dfs(i, D)

print(ans)
