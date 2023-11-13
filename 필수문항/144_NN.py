import sys

input = sys.stdin.readline
N, M = map(int, input().split())

l_N = len(str(N))

if l_N * N <= M:
    for _ in range(N):
        print(N, end="")
else:
    for _ in range(M // l_N):
        print(N, end="")
    print(str(N)[: M % l_N])
