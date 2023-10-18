import sys

input = sys.stdin.readline

N = int(input())


def find(check, now, num):
    while num != 0:
        if num > 0:
            now += 1
            now %= N
            while not check[now]:
                now += 1
                now %= N
            num -= 1
        else:
            now -= 1
            if now < 0:
                now = N + now
            while not check[now]:
                now -= 1
                if now < 0:
                    now = N + now
            num += 1
    return now


papers = list(map(int, input().split()))
check = [True] * N
now = 0
ans = 0
while True:
    if ans == N - 1:
        print(now + 1)
        break
    else:
        print(now + 1, end=" ")
        check[now] = False
        num = papers[now]
        now = find(check, now, num)
        ans += 1
