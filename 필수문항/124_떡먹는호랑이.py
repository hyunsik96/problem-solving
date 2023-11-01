import sys

input = sys.stdin.readline

D, K = map(int, input().split())
# a b a+b a+2b 2a+3b 3a+5b

a = [0] * D
b = [0] * D

a[0] = 1
b[1] = 1

for i in range(2, D):
    a[i] = a[i - 2] + a[i - 1]
    b[i] = b[i - 2] + b[i - 1]

for i in range(1, 100000):
    if (K - a[-1] * i) % b[-1] == 0:
        print(i)
        print((K - a[-1] * i) // b[-1])
        break
