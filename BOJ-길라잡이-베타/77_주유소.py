import sys

input = sys.stdin.readline

n = int(input())

road = list(map(int, input().split()))

price = list(map(int, input().split()))

ans = 0

# 0번째 도시부터 출발
now = 0

# 현재 도시에서 마지막 or 현재보다 싼 도시까지만 주유하면 됨
while True:
    dist = 0
    next = 0
    for i in range(now+1, n):
        dist += road[i-1]
        next = i
        if price[now] > price[i]:
            break
    ans += dist * price[now]
    now = next
    if next == n-1:
        break

print(ans)