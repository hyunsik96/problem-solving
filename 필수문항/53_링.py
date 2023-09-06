import sys

input = sys.stdin.readline

N = int(input())

radius = list(map(int, input().split()))

first = radius[0]

for rad in radius[1:]:
    max_yaksu = 1

    for num in range(min(first, rad), 1, -1):
        if rad % num == 0 and first % num == 0:
            max_yaksu = num
            break

    print(f"{int(first/max_yaksu)}/{int(rad/max_yaksu)}")
