class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_element = float('inf')

        for i in range(len(prices)):
            min_element = min(min_element, prices[i])
            tmp = prices[i] - min_element

            if tmp > profit:
                profit = tmp
        
        return profit
