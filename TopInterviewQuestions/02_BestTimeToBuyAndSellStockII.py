class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        before = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            now = prices[i]
            if before < now:
                ans += now - before
            before = now

        return ans


print(Solution().maxProfit([1, 2, 3, 4, 5]))
