class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        def addCell(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                grid[r][c] != INF
            ):
                return
            
            grid[r][c] = steps
            q.append((r, c))
            visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        steps = 0
        while q:
            size = len(q)
            steps += 1
            for i in range(size):
                r, c = q.popleft()
                visited.add((r, c))
                
                addCell(r + 1, c)
                addCell(r, c + 1)
                addCell(r - 1, c)
                addCell(r, c - 1)

        

