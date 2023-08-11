import sys

input = sys.stdin.readline

n, k = map(int, input().split())

circle = [True] * n
out = []

idx = -1
while len(out) != n:
    count = 0
    while count != k:
        idx = (idx + 1) % n
        if circle[idx]:
            count += 1
    circle[idx] = False
    out.append(idx + 1)

print("<" + ", ".join(map(str, out)) + ">")
