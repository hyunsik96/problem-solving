import sys

input = sys.stdin.readline

sosu = [True] * 1000001
sosu[0] = False
sosu[1] = False
sosu[2] = False  # 짝수의 합중 2가있으면 나머지가 무조건짝수라 소수일수 없기에 제외

for num in range(2, 1001):
    tmp = num * num
    while tmp <= 1000000:
        sosu[tmp] = False
        tmp += num

while True:
    n = int(input())
    if n == 0:
        break

    idx = 3
    while True:
        if sosu[idx] and sosu[n - idx]:
            print(f"{n} = {idx} + {n-idx}")
            break
        idx += 1
