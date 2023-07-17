# 리스트를 마스킹용도로 활용
#  10000개의 수를 담을 배열을 만들고, 입력받을때 인덱스를 늘려주어 그 수의 개수를 담는다.
# 한정된 메모리로 작업할 때 용이

import sys
input = sys.stdin.readline

n = int(input())

# 들어올 수를 인덱스, 들어온 횟수를 값으로 할 배열 생성
a = [0]*10000

# 들어오면 값 증량
for x in range(n):
    a[int(input())-1] += 1

# 값이 0 이 아닌 것만 순서대로 읽기
for y in range(10000):
    if a[y] != 0:
        for z in range(a[y]):
            print(y+1)