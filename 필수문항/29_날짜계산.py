import sys

input = sys.stdin.readline

E, S, M = map(int, input().split())

# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19

# x - 15a / x - 28b / x - 19c
# 15a + E = 28b + S = 19c + M


def check_int(number):
    if isinstance(number, int):
        return True
    elif isinstance(number, float) and number.is_integer():
        return True
    else:
        return False


s_mul = 0

while True:
    if check_int((s_mul * 28 + S - E) / 15) and check_int((s_mul * 28 + S - M) / 19):
        print(s_mul * 28 + S)
        break
    else:
        s_mul += 1
