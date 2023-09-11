import sys

input = sys.stdin.readline

N, K = map(int, input().split())

temp = list(map(int, input().split()))
tmp_sum = sum(temp[:K])
ans = tmp_sum

for i in range(1, N - K + 1):
    tmp_sum += temp[i + K - 1] - temp[i - 1]
    ans = max(ans, tmp_sum)

print(ans)
