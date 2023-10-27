import sys

input = sys.stdin.readline

N = int(input())
homes = sorted(list(map(int, input().split())))
ans = -1
for i in range(1, N):
    diff = (homes[i] - homes[i - 1]) * (2 * i - N)
    if diff > 0 or (diff == 0 and homes[i - 1] != homes[i]):
        ans = i - 1
        break

print(homes[ans])
