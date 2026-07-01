class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c, visit, prevVal):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or 
                (r, c) in visit or
                prevVal > heights[r][c]
            ):
                return
            
            visit.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visit, heights[r][c])
            
        for c in range(COLS):
            dfs(0, c, pacific, -1)
            dfs(ROWS - 1, c, atlantic, -1)
        
        for r in range(ROWS):
            dfs(r, 0, pacific, -1)
            dfs(r, COLS - 1, atlantic, -1)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res