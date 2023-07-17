import sys

input = sys.stdin.readline

num_list = [True] * 10001

for i in range(1, 10001):
    tmp_num = i
    for a in str(i):
        tmp_num += int(a)
    if tmp_num <= 10000:
        num_list[tmp_num] = False

for i in range(1, 10001):
    if num_list[i]:
        print(i)
