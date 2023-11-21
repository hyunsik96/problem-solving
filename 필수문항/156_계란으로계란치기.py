import sys

input = sys.stdin.readline

n = int(input())

eggs = []
for _ in range(n):
    eggs.append(list(map(int, input().split())))
ans = 0


# [내구도, 무게]
def dfs(i):
    global eggs, ans, n

    if i == n:
        broken = 0
        for egg in eggs:
            if egg[0] <= 0:
                broken += 1
        ans = max(ans, broken)
        return

    if eggs[i][0] <= 0:
        dfs(i + 1)
        return

    check = False

    for l in range(n):
        if l == i or eggs[l][0] <= 0:
            continue

        check = True
        eggs[i][0] -= eggs[l][1]
        eggs[l][0] -= eggs[i][1]
        dfs(i + 1)
        eggs[i][0] += eggs[l][1]
        eggs[l][0] += eggs[i][1]

    if not check:
        dfs(i + 1)


dfs(0)
print(ans)
