import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
str_basic = input().rstrip()
lb = len(str_basic)
basic = defaultdict(int)
for c in str_basic:
    basic[c] += 1

ans = 0


def same(word):
    global basic
    for key, value in basic.items():
        word[key] -= value

    check_plus = False
    check_minus = False

    for value in word.values():
        if abs(value) > 1:
            return False
        if value == 1:
            if check_plus:
                return False
            check_plus = True
        if value == -1:
            if check_minus:
                return False
            check_minus = True
    return True


def lw_one(basic_copy, word):
    check = 0
    for key, value in word.items():
        check += abs(value - basic_copy[key])
        if check > 1:
            return False
    return True


def lb_one(word):
    check = 0
    for key, value in basic.items():
        check += abs(value - word[key])
        if check > 1:
            return False
    return True


for _ in range(n - 1):
    str_word = input().rstrip()
    lw = len(str_word)
    word = defaultdict(int)
    for c in str_word:
        word[c] += 1

    if lb == lw:
        if same(word):
            ans += 1

    elif lb + 1 == lw:
        basic_copy = basic.copy()
        if lw_one(basic_copy, word):
            ans += 1

    elif lb == lw + 1:
        if lb_one(word):
            ans += 1


print(ans)
