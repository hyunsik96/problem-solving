import sys

input = sys.stdin.readline

nums = list(map(int, input().split()))

min_num = 9999

for i in range(0, 4):
    tmp_num = (
        nums[i] * 1000
        + nums[(i + 1) % 4] * 100
        + nums[(i + 2) % 4] * 10
        + nums[(i + 3) % 4]
    )
    min_num = tmp_num if min_num > tmp_num else min_num

check = [True] * 10000


def rm_nums(a, b, c, d):
    global check
    tmp = [0] * 4
    final = 9999
    tmp[0] = a * 1000 + b * 100 + c * 10 + d
    tmp[1] = b * 1000 + c * 100 + d * 10 + a
    tmp[2] = c * 1000 + d * 100 + a * 10 + b
    tmp[3] = d * 1000 + a * 100 + b * 10 + c

    final = tmp[0] if final > tmp[0] else final
    final = tmp[1] if final > tmp[1] else final
    final = tmp[2] if final > tmp[2] else final
    final = tmp[3] if final > tmp[3] else final

    for i in range(0, 4):
        if final != tmp[i]:
            check[tmp[i]] = False


ans = 0
for a in range(1, 10):
    for b in range(a, 10):
        for c in range(a, 10):
            for d in range(a, 10):
                tmp = a * 1000 + b * 100 + c * 10 + d
                if check[tmp]:
                    ans += 1
                    if tmp == min_num:
                        print(ans)
                        exit()
                    rm_nums(a, b, c, d)
