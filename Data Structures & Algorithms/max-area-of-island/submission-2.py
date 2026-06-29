class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                grid[r][c] == 0
            ):
                return 0
            
            visited.add((r, c))
            grid[r][c] = 0
            res = 1 + (
                dfs(r + 1, c) + 
                dfs(r, c + 1) +
                dfs(r - 1, c) + 
                dfs(r, c - 1)
            )
            
            return res
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))

        return res