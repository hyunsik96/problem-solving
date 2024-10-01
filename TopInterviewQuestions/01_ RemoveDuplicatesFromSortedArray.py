class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        ans = 1
        start = 0
        end = 1

        while end < len(nums):
            if nums[start] != nums[end]:
                nums[ans] = nums[end]
                ans += 1
                start = end
            end += 1

        return ans


print(Solution().removeDuplicates([1, 2, 3]))
