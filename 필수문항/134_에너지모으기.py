import sys

input = sys.stdin.readline
N = int(input())
W = list(map(int, input().split()))

# (1~N-2) 인덱스를 고를수있음
# N이 3일때까지만 진행

visited = [False] * N
num = N
ans = 0


def dfs(energy):
    global visited, N, W, num, ans

    if num == 2:
        ans = max(ans, energy)
        return

    for i in range(1, N - 1):
        if not visited[i]:
            num -= 1
            visited[i] = True
            lp = i - 1
            rp = i + 1
            while visited[lp]:
                lp -= 1
            while visited[rp]:
                rp += 1
            dfs(energy + W[lp] * W[rp])
            visited[i] = False
            num += 1


dfs(0)

print(ans)
