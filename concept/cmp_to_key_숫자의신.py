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