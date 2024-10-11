class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_num = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] - min_num > ans:
                ans = prices[i] - min_num
            if min_num > prices[i]:
                min_num = prices[i]
        return ans

print(Solution().maxProfit([7,6,4,3,1]))