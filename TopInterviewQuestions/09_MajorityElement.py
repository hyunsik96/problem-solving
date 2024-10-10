class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = int(len(nums) / 2 + 1)
        list.sort(nums)
        i = 1
        now = nums[0]
        n = 1
        while i < len(nums):
            if nums[i] == now:
                n += 1
                if n == l:
                    return now
            else:
                now = nums[i]
                n = 1
            i += 1


print(Solution().majorityElement([2, 2]))
