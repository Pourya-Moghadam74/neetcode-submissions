class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    dp[row][col] += dp[row + 1][col] + dp[row][col + 1]

        return dp[0][0]