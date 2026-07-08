class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]

        for i in range(2, len(cost) + 1):
            tmp = dp[1]
            dp[1] = min(dp[0] + cost[i - 2], dp[1] + cost[i - 1])
            dp[0] = tmp
        
        return dp[1]