class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]
        n = len(cost)

        for i in range(2, n + 1):
            tmp = dp[1]
            dp[1] = min(dp[0] + cost[i - 2], dp[1] + cost[i - 1])
            dp[0] = tmp
        
        return dp[-1]