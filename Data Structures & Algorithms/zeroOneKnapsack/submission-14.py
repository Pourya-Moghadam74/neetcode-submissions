class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0 for _ in range(capacity + 1)] for _ in range(len(profit))]

        for i in range(capacity + 1):
            if weight[0] <= i:
                dp[0][i] = profit[0]
        

        for r in range(1, len(profit)):
            for c in range(capacity + 1):
                newCapacity = c - weight[r]
                if newCapacity >= 0:
                    dp[r][c] = max(profit[r] + dp[r - 1][newCapacity], dp[r - 1][c])
                
                else:
                    dp[r][c] = dp[r - 1][c]


        return dp[-1][-1]