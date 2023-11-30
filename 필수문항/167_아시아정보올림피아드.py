import sys

input = sys.stdin.readline

n = int(input())
countries = [0] * 101
scores = []
for _ in range(n):
    country, num, score = map(int, input().split())
    scores.append((score, country, num))

scores.sort(reverse=True)
ans = 0
for score, country, num in scores:
    if countries[country] < 2:
        print(country, num)
        countries[country] += 1
        if ans == 2:
            break
        else:
            ans += 1
