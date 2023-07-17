import sys
from itertools import combinations

input = sys.stdin.readline

tmp = list(map(int, input().split()))
if tmp[0] == 0: exit()
tmp.pop(0)
result1 = dict.fromkeys(tmp)
result2 = list(result1)
result2.sort()
while result2[0] != 0:
    for b in list(combinations(result2, 6)):
        print(*b)
    tmp = list(map(int, input().split()))
    if tmp[0] == 0: exit()
    tmp.pop(0)
    result1 = dict.fromkeys(tmp)
    result2 = list(result1)
    result2.sort()
    if result2[0] != 0:
        print()