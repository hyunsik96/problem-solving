import sys

input = sys.stdin.readline

K = int(input())
C = int(input())

for _ in range(C):
    M, N = map(int, input().split())
    if M == N:
        print(1)
    elif M > N:
        if M > K - M + 2 + N:
            print(0)
        else:
            print(1)
    else:
        if N > K - N + 1 + M:
            print(0)
        else:
            print(1)
