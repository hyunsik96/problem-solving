import sys
from collections import defaultdict

input = sys.stdin.readline

N, d, k, c = map(int, input().split())

sushi = [0] * N

for i in range(N):
    sushi[i] = int(input())

dic = defaultdict(int)

dic[c] += 1

for i in range(k):
    dic[sushi[i]] += 1

ans = len(dic)

for i in range(1, N):
    if dic[sushi[i - 1]] == 1:
        dic.pop(sushi[i - 1])
    else:
        dic[sushi[i - 1]] -= 1

    dic[sushi[(i + k - 1) % N]] += 1

    ans = max(ans, len(dic))

print(ans)
