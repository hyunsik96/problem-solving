import sys

input = sys.stdin.readline

while True:
    num = input().rstrip()
    if num == "":
        break

    before = num[0]
    ans = 1
    now = 1
    for i in range(1, len(num)):
        if num[i] == before:
            now += 1
            ans = max(ans, now)
        else:
            before = num[i]
            ans = max(ans, now)
            now = 1
    print(ans)
