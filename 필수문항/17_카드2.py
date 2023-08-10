import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

que = deque([x for x in range(1, n + 1)])

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

print(que[0])
