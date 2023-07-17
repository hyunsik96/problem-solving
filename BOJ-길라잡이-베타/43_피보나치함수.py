import sys

input = sys.stdin.readline

t = int(input())

pibo = [[1, 0], [0, 1]]

for i in range(2, 41):
    pibo.append([pibo[i-1][0] + pibo[i-2][0], pibo[i-1][1] + pibo[i-2][1]])

for _ in range(t):
    num = int(input())
    print(*pibo[num])
