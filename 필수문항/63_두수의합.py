import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(0)
    exit()

n_seq = sorted(list(map(int, input().split())))

x = int(input())

ans = 0

for i in range(n):
    if n_seq[i] >= x:
        break
    for m in range(i + 1, n):
        if n_seq[i] + n_seq[m] == x:
            ans += 1
            break
        elif n_seq[i] + n_seq[m] > x:
            break

print(ans)
