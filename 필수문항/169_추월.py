import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
in_list = [input().rstrip() for _ in range(n)]
out_list = deque([input().rstrip() for _ in range(n)])
ans_list = []
now = 0

while out_list:
    if in_list[now] in ans_list:
        now += 1
        continue
    out = out_list.popleft()
    if out not in ans_list:
        if out != in_list[now]:
            ans_list.append(out)
        else:
            now += 1

print(len(ans_list))
