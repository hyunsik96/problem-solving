import sys
from bisect import bisect_left

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    n_list = sorted(list(map(int, input().split())))
    M = int(input())
    m_list = list(map(int, input().split()))
    for num in m_list:
        i = bisect_left(n_list, num)
        if i < N and n_list[i] == num:
            print(1)
        else:
            print(0)
