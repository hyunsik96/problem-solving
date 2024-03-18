import sys

input = sys.stdin.readline

n, m = map(int, input().split())
groups = {}
for _ in range(n):
    tmp = []
    groups[input().rstrip()] = tmp
    nums = int(input())
    for _ in range(nums):
        tmp.append(input().rstrip())
    tmp.sort()

for _ in range(m):
    tmp = input().rstrip()
    if input() == "1\n":
        for group in groups.keys():
            if tmp in groups[group]:
                print(group)
                break
    else:
        for member in groups[tmp]:
            print(member)
