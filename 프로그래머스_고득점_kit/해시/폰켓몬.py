def solution(nums):
    num = len(set(nums))
    if len(nums)//2 >= num:
        return num
    else:
        return len(nums)//2

print(solution([3,3,3,2,2,2]))