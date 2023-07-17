import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip().split())) for x in range(n)]

a = list(combinations([x for x in range(n)], int(n/2)))
ans = -1

for i in range(int(len(a)/2)):
    tmp_m = 0
    tmp_n = 0
    for m in list(combinations(a[i], 2)):
        tmp_m += graph[m[0]][m[1]]
        tmp_m += graph[m[1]][m[0]]
    for n in list(combinations(a[-i-1], 2)):
        tmp_n += graph[n[0]][n[1]]
        tmp_n += graph[n[1]][n[0]]
    if ans is -1:
        if tmp_m - tmp_n >= 0:
            ans = (tmp_m - tmp_n)
        else:
            ans = (tmp_n - tmp_m)
    else:
        if tmp_m - tmp_n >= 0 and tmp_m - tmp_n < ans:
            ans = (tmp_m - tmp_n)
        elif tmp_n - tmp_m >= 0 and tmp_n - tmp_m < ans:
            ans = (tmp_n - tmp_m)
    if ans is 0:
        break

print(ans)