import sys

input = sys.stdin.readline

n = int(input( ))

point = [tuple(map(int, input().strip().split())) for _ in range(n)]

point.sort(key=lambda x: (x[0], x[1]))

for i in point:
    print(i[0], i[1])
