import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for x in range(n)]
home = []
store = []
ans = 3000000

for a in range(n):
    for b in range(n):
        if graph[a][b] is 1:
            home.append((a, b))
        if graph[a][b] is 2:
            store.append((a, b))

for x in list(combinations(store, m)):
    tmp_ans = 0
    for h in home:
        h_dist = 3000
        for y in x:
            tmp = abs(y[0] - h[0]) + abs(y[1] - h[1])
            if tmp < h_dist:
                h_dist = tmp
        tmp_ans += h_dist
    if tmp_ans < ans:
        ans = tmp_ans

print(ans)