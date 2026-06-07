class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0 for _ in range(capacity + 1)] for _ in range(len(weight))]

        for i in range(capacity + 1):
            if weight[0] <= i:
                dp[0][i] = profit[0]
            
        for r in range(1, len(weight)):
            for c in range(capacity + 1):
                take = 0
                if c >= weight[r]:
                    take = profit[r] + dp[r - 1][c - weight[r]]
                
                skip = dp[r-1][c]

                dp[r][c] = max(take, skip)
        

        return dp[-1][-1]