import sys

input = sys.stdin.readline

A, P = map(int, input().split())

D = [A]

while True:
    next_num = 0
    for num in str(D[-1]):
        next_num += int(num) ** P
    if next_num in D:
        print(D.index(next_num))
        break
    else:
        D.append(next_num)
