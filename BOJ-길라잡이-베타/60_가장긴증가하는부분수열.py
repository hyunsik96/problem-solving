import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans_list = [1]*n

for x in range(n):
    tmp_max = 0
    for i in range(x):
        if a[i] < a[x]:
            tmp_max = max(ans_list[i], tmp_max)
    ans_list[x] = tmp_max + 1

print(max(ans_list))