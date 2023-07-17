import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

if n == 1: # n이 1이면 걍 1 출력하고 종료
    print(int(input()))
    exit()

# 이제 n이 1인경우 없으니 2개 미리 받고 왼쪽 오른쪽 힙 하나씩 채우고 시작
first = int(input())
print(first)
second = int(input())

l_heap = [-min(first, second)] # 가운데 값의 왼쪽이 가장 큰 최대힙
r_heap = [max(first, second)] # 가운데 값의 오른쪽이 가장 작은 최소힙

print(-l_heap[0])

# 왼쪽 힙이 항상 오른쪽 힙보다 한개 더 많거나 개수가 같도록 추가
# 그래야 개수가 같던 왼쪽이 하나많던 항상 왼쪽 최대값이 중간값
for i in range(n-2):
    num = int(input())
    left = -l_heap[0]
    right = r_heap[0]

    # 총 개수상 홀수번째 수가 추가될 때는 왼쪽 힙 개수가 하나 늘어야함
    if i % 2 == 0:
        if right >= num:    # 오른쪽 최소값보다 작거나같으면 오른쪽거 신경 안쓰고 왼쪽힙에 넣으면 됨
            heappush(l_heap, -num)
        else:               # 오른쪽보다 크면 왼쪽거 넣을 차례라 오른쪽거 하나 빼서 왼쪽 보내고 오른쪽에 넣어야함
            heappush(l_heap, -heappop(r_heap))
            heappush(r_heap, num)

    # 짝수는 오른쪽 힙 개수 늘어야함
    else:
        if left <= num:     # 왼쪽 최대값보다 크거나 같으면 왼쪽거 신경 안쓰고 오른쪽힙에 넣으면 됨
            heappush(r_heap, num)
        else:               # 왼쪽보다 작으면 오른쪽거 넣을 차례라 왼쪽거 빼서 오른쪽 보내고 왼쪽 넣어야함
            heappush(r_heap, -heappop(l_heap))
            heappush(l_heap, -num)
    
    # 우선순위큐 자료구조상 0번째인덱스가 최소인것은 보장이므로 항상 왼쪽 최대값은 0번째인덱스에 -한거
    print(-l_heap[0])