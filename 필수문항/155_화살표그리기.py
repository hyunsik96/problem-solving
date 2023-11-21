import sys

input = sys.stdin.readline

n = int(input())
points = []
for _ in range(n):
    x, color = map(int, input().split())
    points.append((color, x))
points.sort()
answer = 0
for i in range(n):
    ans = 100000
    if 0 < i and points[i][0] == points[i - 1][0]:
        ans = points[i][1] - points[i - 1][1]
    if i < n - 1 and points[i][0] == points[i + 1][0]:
        ans = min(ans, points[i + 1][1] - points[i][1])
    answer += ans
print(answer)
