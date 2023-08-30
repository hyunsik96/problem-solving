import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    cate_dic = defaultdict(int)
    ans = 1
    for _ in range(N):
        name, category = input().split()
        cate_dic[category] += 1
    for count in cate_dic.values():
        ans *= count + 1
    print(ans - 1)
