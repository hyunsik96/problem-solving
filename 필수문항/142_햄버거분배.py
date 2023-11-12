import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

table = list(input().rstrip())
que = deque([])
ans = 0

for i in range(N):
    if table[i] == "H":
        que.append(i)
    elif table[i] == "P":
        check = False
        while que:
            h = que.popleft()
            if i - h <= K:
                ans += 1
                check = True
                break
        if not check:
            for l in range(i + 1, min(i + K + 1, N)):
                if table[l] == "H":
                    ans += 1
                    table[l] = "X"
                    break
print(ans)
