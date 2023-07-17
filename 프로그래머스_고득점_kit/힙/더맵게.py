from heapq import heappush, heappop, heapify

def solution(scoville, K):
    heapify(scoville)
    answer = 0

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville, a + b * 2)
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))