import sys

input = sys.stdin.readline

K = int(input())
stack = []
ans = 0

for _ in range(K):
    num = int(input())
    if num == 0 and stack:
        ans -= stack.pop()
    else:
        ans += num
        stack.append(num)

print(ans)
