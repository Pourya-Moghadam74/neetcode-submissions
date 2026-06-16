class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        if n == 1:
            return 1

        for i in range(2, n):
            tmp = dp[1]
            dp[1] = dp[1] + dp[0]
            dp[0] = tmp
        
        return dp[1]