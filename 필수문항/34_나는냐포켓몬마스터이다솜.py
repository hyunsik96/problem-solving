import sys

input = sys.stdin.readline

N, M = map(int, input().split())

monsters = [""] * (N + 1)
mon_dict = {}

for i in range(1, (N + 1)):
    tmp = input().rstrip()
    monsters[i] = tmp
    mon_dict[tmp] = i

for _ in range(M):
    prob = input().rstrip()
    if prob.isdigit():
        print(monsters[int(prob)])
    else:
        print(mon_dict[prob])
