def solution(stones, k):
    left = 1
    right = max(stones) # 돌의 가장큰 수보다 많이 건널 수 없음
    while left <= right:
        mid = (left + right) // 2
        cnt = 0 # 몇번 건너뛰고 있는지 체크하여 k와 비교
        for s in stones:
            if s - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
        
    return left

# 시간초과
# def solution(stones, k):
#     answer = 0
#     now = -1
#     jump = 1
#     while True:
#         try:
#             if stones[now+jump]:
#                 stones[now+jump] -= 1
#                 now = now+jump
#                 jump = 1
#             else:
#                 if jump == k:
#                     break
#                 jump += 1
#         except:
#             answer += 1
#             now = -1
#             jump = 1
#     return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))