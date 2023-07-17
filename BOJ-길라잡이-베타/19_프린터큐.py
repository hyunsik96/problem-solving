import sys
from collections import deque


input = sys.stdin.readline

case_num = int(input())

for _ in range(case_num):
    ans = 0
    n, i = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    while(queue):
        if len(queue) == 1:
            print(ans+1)
            break
        tmp = queue.popleft()
        if tmp >= max(queue):
            ans += 1
            if i == 0:
                print(ans)
                break
            i -= 1
        else:
            queue.append(tmp)
            if i == 0:
                i = len(queue)-1
            else:
                i -= 1