class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        dp[rows - 1][cols - 1] = 1

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    dp[row][col] += dp[row][col + 1] + dp[row + 1][col]

        return dp[0][0]