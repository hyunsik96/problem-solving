import sys
from functools import cmp_to_key

input = sys.stdin.readline

k, n = map(int, input().split())
nums = [0]*k
ans = ""
check = True # 가장 큰 수가 중복일 때 한번만 반복시키기 위한 flag

for i in range(k):
    nums[i] = int(input())

max_num = max(nums)

def compare(x, y):
    if str(x)+str(y) > str(y)+str(x):
        return -1
    elif str(x)+str(y) == str(y)+str(x):
        return 0
    else:
    	return 1

# 리스트를 각 요소를 붙였을 때 어느 경우가 더 큰 수가 되는지를 기준으로 정렬
nums.sort(key=cmp_to_key(compare))

for x in nums:
    # 가장 큰 수만 초과횟수만큼 반복
    if check and x == max_num:
        for _ in range(n-k):
            ans += str(x)
        check = False
    ans += str(x)

print(ans)

# 9로 채웠던 것 때문에 발생하는 반례가 있음 ㄲㅂ
# import sys
# import math
# from heapq import heappop, heappush

# input = sys.stdin.readline

# k, n = map(int, input().split())

# nums = [] # 크기 큰 순서대로 최대 힙
# len_max = [0, 0]

# # 최대 수 1,000,000,000 의 자릿수까지 모두 표현할 것
# # 이하 자리수는 나머지 자릿수를 9로 채움
# for i in range(k):
#     num = int(input())
#     num_len = int(math.log10(num))
#     num = num * 10**(9 - num_len)
#     for m in range(9 - num_len):
#         num += 10**m * 9
    
#     # 반복시킬 자릿수 가장 큰 수중 제일 크게 값을 출력해줄녀석 저장
#     if len_max[0] < num_len or (len_max[0] == num_len and len_max[1] < num):
#         len_max[0] = num_len
#         len_max[1] = num

#     heappush(nums, [-num, -num_len])

# ans = ""
# check = True

# while nums:
#     tmp_num, tmp_len = heappop(nums)

#     # 반복시킬 수인지 확인
#     if check and -tmp_num == len_max[1]:
#         for _ in range(n-k):
#             tmp_str = str(-tmp_num)
#             ans += tmp_str[:-tmp_len+1]
#         check = False
    
#     tmp_str = str(-tmp_num)
#     ans += tmp_str[:-tmp_len+1]

# print(ans)