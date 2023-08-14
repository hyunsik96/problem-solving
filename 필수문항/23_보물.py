import sys

input = sys.stdin.readline

N = int(input())
S = 0

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

for i in range(N):
    S += A[i] * B[i]

print(S)
