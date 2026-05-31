class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = 0
        res = 0
        for i in range(1, len(prices)):
            dp = max(0, dp + prices[i] - prices[i - 1])
            res = max(res, dp)
        return res