import sys

m, n = map(int, sys.stdin.readline().split())

a = max(m, n)
b = min(m, n)

ans_max = 1
ans_min = a * b

for i in range(b, 1, -1):
    if a % i is 0 and b % i is 0:
        ans_max = i
        break

for k in range(a, a*b):
    if k % a is 0 and k % b is 0:
        ans_min = k
        break

print(ans_max)
print(ans_min)