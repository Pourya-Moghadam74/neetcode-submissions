class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        rows = len(profit)
        cols = capacity
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows)]

        for i in range(cols + 1):
            if weight[0] <= i:
                dp[0][i] = profit[0]

        for i in range(1, rows):
            for j in range(cols + 1):
                skip = dp[i - 1][j]

                include = 0
                newCap = j - weight[i]
                if newCap >= 0:
                    include = profit[i] + dp[i - 1][newCap]
                
                dp[i][j] = max(skip, include)

        return dp[rows -1][cols]