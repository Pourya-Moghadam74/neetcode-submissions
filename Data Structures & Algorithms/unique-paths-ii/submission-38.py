class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {}
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            
            if obstacleGrid[r][c] == 1:
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            if (r, c) in cache:
                return cache[(r, c)]
            
            res = dfs(r + 1, c) + dfs(r, c + 1)
            cache[(r, c)] = res

            return res
        
        return dfs(0, 0)

