import sys

input = sys.stdin.readline

n = int(input())

n_list = list(set(map(int, input().split())))

n_list.sort()

for a in n_list:
    print(a, end=' ')