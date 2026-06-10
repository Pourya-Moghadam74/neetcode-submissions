class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {}
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        def dfs(i, j):
            if i == rows - 1 and j == cols - 1:
                return 1 if obstacleGrid[i][j] == 0 else 0
            
            if i >= rows or j >= cols:
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            if obstacleGrid[i][j] == 1:
                cache[(i, j)] = 0
                return cache[(i, j)]
            
            right = dfs(i, j + 1)
            down = dfs(i + 1, j)

            cache[(i, j)] = right + down
            return cache[(i, j)]
        
        return dfs(0, 0)