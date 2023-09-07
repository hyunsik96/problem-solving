import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())

b_list = deque([[B, 1]])

while b_list:
    b_pop, count = b_list.popleft()
    if b_pop == A:
        print(count)
        exit()
    b_str = str(b_pop)
    if b_str[-1] == "1" and b_str != "1":
        b_list.append([int(b_str[:-1]), count + 1])
    if b_pop % 2 == 0:
        b_list.append([int(b_pop / 2), count + 1])

print(-1)
