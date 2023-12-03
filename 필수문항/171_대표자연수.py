import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

min_num = nums[0]
max_num = nums[0]

for i in range(1, n):
    min_num = min(min_num, nums[i])
    max_num = max(max_num, nums[i])


def binary_search(nums, start, end):
    mid = (start + end) // 2
    total = 0
    total_minus = 0
    total_plus = 0
    for num in nums:
        total += abs(num - mid)
        total_minus += abs(num - mid + 1)
        total_plus += abs(num - mid - 1)

    if total_minus <= total:
        return binary_search(nums, start, mid - 1)
    elif total_plus < total:
        return binary_search(nums, mid + 1, end)
    else:
        return mid


print(binary_search(nums, min_num, max_num))
