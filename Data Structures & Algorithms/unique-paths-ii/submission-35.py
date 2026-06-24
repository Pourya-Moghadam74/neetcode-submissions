class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        dp = [0] * COLS
        dp[COLS - 1] = 0 if obstacleGrid[ROWS - 1][COLS - 1] == 1 else 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):

                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                
                else:
                    if c <= COLS - 2:
                        dp[c] += dp[c + 1]


        return dp[0]
                
