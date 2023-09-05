import sys

input = sys.stdin.readline

N = int(input())

empty = 1
one_side = 1

for i in range(1, N):
    tmp_empty = empty
    tmp_one_side = one_side
    empty = tmp_empty + 2 * tmp_one_side
    one_side = tmp_empty + tmp_one_side

print((empty + 2 * one_side) % 9901)
