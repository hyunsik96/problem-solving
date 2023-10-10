import sys

input = sys.stdin.readline


def check(bingo, num):
    global ans
    x, y = 0, 0
    for a in range(5):
        try:
            b = bingo[a].index(num)
            x, y = a, b
            break
        except:
            continue

    bingo[x][y] = 0

    c = True
    for n in bingo[x]:
        if n != 0:
            c = False
            break
    if c:
        ans += 1
        if ans >= 3:
            return True

    c = True
    for i in range(5):
        if bingo[i][y] != 0:
            c = False
            break
    if c:
        ans += 1
        if ans >= 3:
            return True

    if x == y:
        c = True
        for i in range(5):
            if bingo[i][i] != 0:
                c = False
                break
        if c:
            ans += 1
        if ans >= 3:
            return True

    if x + y == 4:
        c = True
        for i in range(5):
            if bingo[i][4 - i] != 0:
                c = False
                break
        if c:
            ans += 1
        if ans >= 3:
            return True

    return False


bingo = [list(map(int, input().split())) for _ in range(5)]
ans = 0
for i in range(5):
    count = 1
    for num in map(int, input().split()):
        if check(bingo, num):
            print(5 * i + count)
            exit()
        else:
            count += 1
