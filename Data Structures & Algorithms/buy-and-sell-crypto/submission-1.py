class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = float('inf')

        for item in prices:
            minPrice = min(minPrice, item)
            profit = max(profit, item - minPrice)
        
        return profit