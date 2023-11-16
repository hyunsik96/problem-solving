import sys

input = sys.stdin.readline

N, K = map(int, input().split())
minimum = K * (K + 1) / 2
if N < minimum:
    print(-1)
else:
    N = (N - minimum) % K
    if N == 0:
        print(K - 1)
    else:
        print(K)
