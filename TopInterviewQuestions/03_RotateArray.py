class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        store = nums.copy()
        len_nums = len(nums)

        for i in range(len_nums):
            nums[(k+i) % len_nums] = store[i]


Solution().rotate([1,2,3,4,5,6,7], 3)