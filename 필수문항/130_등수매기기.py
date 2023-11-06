import sys

input = sys.stdin.readline

N = int(input())
students = [int(input()) for _ in range(N)]
students.sort()

ans = 0

for i in range(N):
    ans += abs(students[i] - i - 1)

print(ans)
