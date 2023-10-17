import sys
from bisect import bisect_left

input = sys.stdin.readline

T = int(input())


def binary_search(n_list, num):
    lp, rp = 0, len(n_list) - 1
    while lp <= rp:
        mid = (lp + rp) // 2
        if n_list[mid] == num:
            return True
        elif n_list[mid] > num:
            rp = mid - 1
        else:
            lp = mid + 1
    return False


for _ in range(T):
    N = int(input())
    n_list = sorted(list(map(int, input().split())))
    M = int(input())
    m_list = list(map(int, input().split()))
    for num in m_list:
        if binary_search(n_list, num):
            print(1)
        else:
            print(0)
