class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        temp = [51]*len(nums)
        i = 0
        for num in nums:
            if num != val:
                temp[i] = num
                i += 1
        
        for idx in range(len(nums)):
            if temp[idx] == 51:
                break
            nums[idx] = temp[idx]
        
        return i

print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))