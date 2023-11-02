import sys

input = sys.stdin.readline

n = int(input())

friend = []
graph = [[False] * n for _ in range(n)]

for num in range(n):
    word = input().rstrip()
    tmp = []
    for i in range(n):
        if word[i] == "Y":
            tmp.append(i)
            graph[num][i] = True
    friend.append(tmp)

for i in range(n):
    for k in friend[i]:
        for kk in friend[k]:
            graph[i][kk] = True
ans = 0
for f in graph:
    f_ans = 0
    for tiny in f:
        if tiny == True:
            f_ans += 1
    ans = max(ans, f_ans)

print(max(0, ans - 1))
