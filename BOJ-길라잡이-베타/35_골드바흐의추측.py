import sys

input = sys.stdin.readline

sosu = [True]*1000001
sosu[0] = False
sosu[1] = False
sosu[2] = False # 홀수소수만 취급

for x in range(2, 500001):
    a = 2 * x
    while a < 1000001:
        sosu[a] = False
        a += x

tmp = int(input())
while tmp != 0:

    for x in range(3, int(tmp/2)+1):
        if sosu[x] and sosu[tmp-x]:
            print(f'{tmp} = {x} + {tmp-x}')
            break
        if x == int(tmp/2):
            print("Goldbach's conjecture is wrong.")

    tmp = int(input())
