import sys

input = sys.stdin.readline

n = int(input())


def fibo(n):
    before = 0
    now = 1
    i = 1
    tmp = 0
    while i < n:
        tmp = before
        before = now
        now = (tmp + now) % 1000000000
        i += 1
    return now


if n > 0:
    print(1)
    print(fibo(n))
elif n < 0:
    n *= -1
    if n % 2 == 1:
        print(1)
    else:
        print(-1)
    print(fibo(n))
else:
    print(0)
    print(0)
