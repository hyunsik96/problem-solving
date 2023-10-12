import sys

input = sys.stdin.readline

N = int(input())

left = list(map(int, input().split()))
ans = [0] * N

n_list = [n for n in range(N)]

for i in range(N):
    ans[n_list[left[i]]] = i + 1
    n_list.pop(left[i])

print(*ans, sep=" ")
