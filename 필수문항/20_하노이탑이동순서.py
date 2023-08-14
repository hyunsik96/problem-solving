import sys

N = int(sys.stdin.readline())
ans = 0
move_list = []


def one_two_three(a, b):
    check = [False, True, True, True]
    check[a] = False
    check[b] = False
    return check.index(True)


def move(n, dep, arr):
    global ans
    if n > 1:
        move(n - 1, dep, one_two_three(dep, arr))
    move_list.append([dep, arr])
    ans += 1
    if n > 1:
        move(n - 1, one_two_three(dep, arr), arr)


move(N, 1, 3)

print(ans)
for sublist in move_list:
    print(*sublist)
