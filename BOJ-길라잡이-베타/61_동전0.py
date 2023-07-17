import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = 0

for x in a[::-1]:
    ans += k // x
    k = k % x

print(ans)