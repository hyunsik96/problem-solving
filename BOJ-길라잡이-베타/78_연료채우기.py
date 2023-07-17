import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())

# 주유소까지 거리, 기름
station = [[0, 0] for _ in range(n+1)]

for i in range(n):
    a, b = map(int, input().split())
    station[i][0] = a
    station[i][1] = b

# 마을까지 거리 l, 남은 기름 p
l, p = map(int, input().split())

# 마지막 도착지에 대한 정보를 넣어두어 아래 for문 끝날 때 heap에 쌓아둔 지나친 주유소들 한번 다 연산은 하게끔 해줌
station[-1][0] = l
station[-1][1] = 0

station.sort()

ans = 0

heap = []

# 현재 위치
now = 0

# 매번 다음 도착 가능한 주유소를 뽑고 생각
for x, y in station:
    while heap and p < x - now:
        station_oil, station_dist = heappop(heap)
        p = p - station_oil - station_dist + now
        now = station_dist
        ans += 1

    # 다음 주유소까지 못가는 경우
    if p < x - now:
        print(-1)
        exit()

    # 남은기름으로 목적지까지 갈 수 있는 경우
    if p >= l - now:
        print(ans)
        exit()

    # 남은기름 + 다음 주유소 기름으로 목적지 갈 수 있는 경우
    if p + y >= l - now:
        print(ans + 1)
        exit()

    heappush(heap, [-y, x])

print(-1)




# 메모리 초과, 1개들리는 경우부터 브루트 포스, 찾는즉시 프로그램 종료
# import sys
# from itertools import combinations

# input = sys.stdin.readline

# n = int(input())

# # 주유소까지 거리, 기름
# station = [[0, 0] for _ in range(n)]
# arr = [i for i in range(n)]

# for i in range(n):
#     a, b = map(int, input().split())
#     station[i][0] = a
#     station[i][1] = b

# # 마을까지 거리 l, 남은 기름 p
# l, p = map(int, input().split())

# if l <= p:
#     print(0)
#     exit()

# for x in range(1, n+1):
#     for stop in list(combinations(arr, x)):
#         oil = p # 남은 기름
#         now = 0 # 현재 위치
#         for z in range(len(stop)):
#             if oil >= station[stop[z]][0] - now:
#                 oil = oil - station[stop[z]][0] + station[stop[z]][1]
#                 now += station[stop[z]][0]
#                 if z == len(stop) - 1 and oil >= l - now:
#                     print(x)
#                     exit()
#             else:
#                 break

# print(-1)