import sys
from itertools import combinations

input = sys.stdin.readline
N, S  = map(int, input().split())
myInput = list(map(int, input().split()))



def myfuc(a):
    cnt = 0
    if  N == 1:
        if myInput[0] == 0:
            print(1)
            return
    for i in range(1, len(a)+1):
        comb_list = list(combinations(a, i))
        for comb in comb_list:
            list(comb)
        set(comb_list)

        for comb in comb_list:
            if sum(comb) == S:
                cnt += 1

    print(cnt)

myfuc(myInput) 