class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        dp[n - 1] = 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                # if row < m - 1:
                #     dp[col] += dp[col]
                
                if col < n - 1:
                    dp[col] += dp[col + 1]
            
        
        return dp[0]