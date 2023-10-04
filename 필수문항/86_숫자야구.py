import sys

input = sys.stdin.readline

N = int(input())

ans = 504
check = [True] * 504
total = [[0, 0, 0] for _ in range(504)]
i = 0

while i < 504:
    for l in range(1, 10):
        for m in range(1, 10):
            for n in range(1, 10):
                if l == m or l == n or m == n:
                    continue
                total[i][0], total[i][1], total[i][2] = l, m, n
                i += 1

for _ in range(N):
    num, s, b = input().split()
    num = [int(num[0]), int(num[1]), int(num[2])]
    s, b = int(s), int(b)

    i = 0
    tmp_s = 0
    tmp_b = 0
    while i < 504:
        if not check[i]:
            i += 1
            continue
        tmp_s = 0
        tmp_b = 0
        for l in range(3):
            if num[l] == total[i][l]:
                tmp_s += 1
            elif num[l] in total[i]:
                tmp_b += 1
        if tmp_s != s or tmp_b != b:
            check[i] = False
            ans -= 1
        i += 1

print(ans)
