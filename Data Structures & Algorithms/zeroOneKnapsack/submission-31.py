class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0 for i in range(capacity + 1)] for _ in range(len(profit))]

        for c in range(1, capacity + 1):
            if weight[0] <= c:
                dp[0][c] = profit[0]


        for i in range(1, len(profit)):
            for c in range(1, capacity + 1):
                if weight[i] <= c:
                    leftCap = c - weight[i]
                    dp[i][c] = max(profit[i] + dp[i - 1][leftCap], dp[i - 1][c])
                else:
                    dp[i][c] = dp[i - 1][c]
        
        return dp[-1][-1]