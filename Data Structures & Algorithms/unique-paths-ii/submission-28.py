class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        cache = {}

        def dfs(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            
            if obstacleGrid[r][c] == 1:
                return 0
            
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            if (r, c) in cache:
                return cache[(r, c)]    
            
            right = dfs(r + 1, c)
            down = dfs(r, c + 1)
            cache[(r, c)] = right + down
            return cache[(r, c)]
        
        return dfs(0, 0)
