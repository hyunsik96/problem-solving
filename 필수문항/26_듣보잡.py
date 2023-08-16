import sys
import bisect

input = sys.stdin.readline

N, M = map(int, input().split())

n_list = sorted([input().rstrip() for _ in range(N)])

ans_list = []

for _ in range(M):
    tmp_m = input().rstrip()
    index = bisect.bisect_left(n_list, tmp_m)

    if index < len(n_list) and n_list[index] == tmp_m:
        ans_list.append(tmp_m)

print(len(ans_list))
print(*sorted(ans_list), sep="\n")
