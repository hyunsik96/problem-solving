import sys
import math

input = sys.stdin.readline


def get_b(i, k, m):
    global dolls
    s = 0
    for idx in range(i, i + k):
        s += (dolls[idx] - m) ** 2
    if s / k == 0.888888888888889:
        print("!!!")
    return s / k


n, k = map(int, input().split())
dolls = list(map(int, input().split()))
s = sum(dolls[:k])
ans = get_b(0, k, s / k)

tmp_sum = s

for i in range(1, n - k + 1):
    tmp_sum += dolls[k + i - 1]
    ans = min(ans, get_b(0, k + i, tmp_sum / (k + i)))


for now in range(1, n - k + 1):
    s -= dolls[now - 1] - dolls[now + k - 1]

    ans = min(ans, get_b(now, k, s / k))
    tmp_sum = s

    for i in range(1, n - k + 1 - now):
        tmp_sum += dolls[now + k + i - 1]
        ans = min(ans, get_b(now, k + i, tmp_sum / (k + i)))
print(math.sqrt(ans))
