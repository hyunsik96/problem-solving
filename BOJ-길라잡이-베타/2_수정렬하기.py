import sys

input = sys.stdin.readline

a = int(input())
b = []

for x in range(a):
    b.append(int(input()))

b.sort()

for y in b:
    print(y)