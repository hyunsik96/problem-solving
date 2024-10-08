class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        removed = [0]*len(nums)
        if len(nums) < 3:
            return len(nums)
        removed[0] = nums[0]
        removed[1] = nums[1]
        now = 2
        ans = 2
        for i in range(2, len(nums)):
            while now < len(nums):
                if not(removed[i-2] == removed [i-1] == nums[now]):
                    removed[i] = nums[now]
                    ans += 1
                    now += 1
                    break
                now += 1
        for i in range(ans):
            nums[i] = removed[i]
        return ans

print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))