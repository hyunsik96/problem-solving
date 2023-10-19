import sys

input = sys.stdin.readline


def check(nums, num):
    ones = 1
    ans = 1
    while ones < num:
        ones = ones * 10 + 1
        ans += 1
    while ones % num != 0:
        ones = (ones * 10 + 1) % num
        ans += 1
    nums[num] = ans


nums = [1000000] * 10001

for num in range(1, 10001):
    if num % 2 != 0 and num % 5 != 0:
        check(nums, num)

while True:
    try:
        print(nums[int(input())])
    except:
        break
