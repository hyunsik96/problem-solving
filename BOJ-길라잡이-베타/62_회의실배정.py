import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())
time_table = []

# 끝나는시간 빠른 순서대로 우선순위 큐에 삽입
for _ in range(n):
    a, b = map(int, input().split())
    heappush(time_table, [b, a])

end_time = 0
ans = 0

# 우선순위 큐에서 나오는 녀석의 시작시간과 이전 끝 시간비교
while time_table:
    tmp = heappop(time_table)
    if tmp[1] >= end_time:
        end_time = tmp[0]
        ans += 1

print(ans)