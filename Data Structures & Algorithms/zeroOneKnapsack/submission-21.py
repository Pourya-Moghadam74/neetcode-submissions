class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]

        for i in range(capacity + 1):
            dp[0][i] = profit[0] if weight[0] <= i else 0
        
        for r in range(1, n):
            for c in range(capacity + 1):
                take = 0
                if c >= weight[r]:
                    take = profit[r] + dp[r - 1][c - weight[r]]
                
                skip = dp[r - 1][c]
                dp[r][c] = max(take, skip)
        return dp[-1][-1]