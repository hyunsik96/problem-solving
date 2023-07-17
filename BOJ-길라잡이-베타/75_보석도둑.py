import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, k = map(int, input().split())

jewel = []
ans = 0

for _ in range(n):
    m, v = map(int, input().split())
    heappush(jewel, [m, v])

bag = [0]*k # 가방이 수용가능한 무게로 정렬

# check_bag = [True]*k # i 번째 가방이 사용가능한지 여부
# bag_left = k # 가방 k 개중 사용가능한 가방의 개수

for i in range(k):
    bag[i] = int(input())

bag.sort()

mini_jewel = []

for x in bag:
    while jewel and x >= jewel[0][0]:
        heappush(mini_jewel, -heappop(jewel)[1])
    if mini_jewel:
        ans -= heappop(mini_jewel)


# 시간초과
# while bag_left:
#     jewel_v, jewel_m = heappop(jewel)
#     for i in range(k):
#         if check_bag[i] and bag[i] >= jewel_m:
#             ans += -jewel_v
#             bag_left -= 1
#             check_bag[i] = False
#             break

print(ans)