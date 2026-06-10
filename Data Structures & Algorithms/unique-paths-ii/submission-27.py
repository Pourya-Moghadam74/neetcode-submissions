class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        dp[rows - 1][cols - 1] = 1 - grid[rows - 1][cols - 1]

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if grid[r][c] == 1:
                    dp[r][c] = 0
                
                else:
                    dp[r][c] += dp[r + 1][c] + dp[r][c + 1]
        

        return dp[0][0]
