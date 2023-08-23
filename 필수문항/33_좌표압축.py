import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())

num_list = list(map(int, input().split()))

sorted_list = sorted(set(num_list))

for i in range(N):
    num_list[i] = bisect_left(sorted_list, num_list[i])

print(*num_list, sep=" ")
