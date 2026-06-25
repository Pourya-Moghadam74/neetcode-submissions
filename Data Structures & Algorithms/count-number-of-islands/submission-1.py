class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            
            if grid[i][j] == "0":
                return

            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        
        return res
            
