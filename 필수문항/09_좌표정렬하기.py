import sys
from functools import cmp_to_key

input = sys.stdin.readline

n = int(input())

xy = []

for _ in range(n):
    xy.append(list(map(int, input().split())))


def compare(x, y):
    if x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    elif x[1] < y[1]:
        return -1
    elif x[1] > y[1]:
        return 1
    else:
        return 0


xy.sort(key=cmp_to_key(compare))

for point in xy:
    print(*point)
