import sys

input = sys.stdin.readline

N = int(input())

num = int(input())

recs = list(map(int, input().split()))
order = 1
r_list = []  # [count, order, person]

for r in recs:
    check = False
    for i in range(len(r_list)):
        if r_list[i][2] == r:
            r_list[i][0] += 1
            check = True
            break
    if not check:
        if len(r_list) == N:
            r_list.pop(0)
        r_list.append([1, order, r])
        order += 1
    r_list.sort()

ans = []
for r in r_list:
    ans.append(r[2])
ans.sort()
print(*ans, sep=" ")
