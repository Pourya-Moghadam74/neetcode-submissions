class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cols = capacity + 1
        rows = len(profit)
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(cols):
            dp[0][i] = profit[0] if i >= weight[0] else 0

        for r in range(1, rows):
            for c in range(cols):
                take = 0
                if c >= weight[r]:
                    take = profit[r] + dp[r - 1][c - weight[r]]
                
                skip = dp[r - 1][c]

                dp[r][c] = max(take, skip)
        
        return dp[-1][-1]

