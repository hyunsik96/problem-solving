class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        temp = sorted(nums1[:m] + nums2[:n])
        if len(nums1) > m + n:
            for _ in range(len(nums1) - m - n):
                nums1.pop(-1)
        else:
            for _ in range(-len(nums1) + m + n):
                nums1.append(0)
        for i in range(m + n):
            nums1[i] = temp[i]


Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
