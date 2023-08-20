import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_list = list(map(int, input().split()))
sum_list = [0] * N
sum_list[0] = num_list[0]

for i in range(1, N):
    sum_list[i] = sum_list[i - 1] + num_list[i]

for _ in range(M):
    start, end = map(int, input().split())
    if start > 1:
        print(sum_list[end - 1] - sum_list[start - 2])
    else:
        print(sum_list[end - 1])
