import sys

input = sys.stdin.readline

xl, yl = map(int, input().split())

n = int(input())
stores = [list(map(int, input().split())) for _ in range(n)]

d, l = map(int, input().split())
ans = 0

for i in range(n):
    sd, sl = stores[i]
    if d == 1:
        if sd == 1:
            ans += abs(l - sl)
        elif sd == 2:
            if l + sl <= xl * 2 - l - sl:
                ans += yl + l + sl
            else:
                ans += yl + 2 * xl - l - sl
        elif sd == 3:
            ans += l + sl
        else:
            ans += xl - l + sl
    elif d == 2:
        if sd == 2:
            ans += abs(l - sl)
        elif sd == 1:
            if l + sl <= xl * 2 - l - sl:
                ans += yl + l + sl
            else:
                ans += yl + 2 * xl - l - sl
        elif sd == 3:
            ans += l + yl - sl
        else:
            ans += xl - l + yl - sl
    elif d == 3:
        if sd == 1:
            ans += l + sl
        elif sd == 2:
            ans += yl - l + sl
        elif sd == 3:
            ans += abs(l - sl)
        else:
            if l + sl <= 2 * yl - l - sl:
                ans += l + sl + xl
            else:
                ans += 2 * yl - l - sl + xl
    else:
        if sd == 1:
            ans += l + xl - sl
        elif sd == 2:
            ans += yl - l + xl - sl
        elif sd == 4:
            ans += abs(l - sl)
        else:
            if l + sl <= 2 * yl - l - sl:
                ans += l + sl + xl
            else:
                ans += 2 * yl - l - sl + xl

print(ans)
