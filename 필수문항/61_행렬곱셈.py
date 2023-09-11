import sys

input = sys.stdin.readline

N, M = map(int, input().split())

left = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())

right = [list(map(int, input().split())) for _ in range(M)]

ans = [[0] * K for _ in range(N)]

for a in range(N):
    for b in range(K):
        for c in range(M):
            ans[a][b] += left[a][c] * right[c][b]

for row in ans:
    print(*row, sep=" ")
