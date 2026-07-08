class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                grid[r][c] == 0
            ):
                return 0
            
            visited.add((r, c))

            tmp = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                tmp += dfs(nr, nc)

            return tmp

        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c)) 
        
        return res
