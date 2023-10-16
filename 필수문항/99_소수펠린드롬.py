import sys
import math

input = sys.stdin.readline

N = int(input())

sosu = [True] * 1003002
sosu[0] = False
sosu[1] = False

for i in range(2, int(math.sqrt(1003002) + 1)):
    num = i**2
    while num < 1003002:
        sosu[num] = False
        num += i


def check(num):
    num = str(num)
    lp, rp = 0, len(num) - 1

    while True:
        if lp >= rp:
            return True

        if num[lp] == num[rp]:
            lp += 1
            rp -= 1
        else:
            return False


for i in range(N, 1003002):
    if sosu[i] and check(i):
        print(i)
        break
