class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()
        visited = set()

        def addRow(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                grid[r][c] == -1
            ):
                return
            
            q.append((r, c))
            visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = steps
                addRow(r + 1, c)
                addRow(r, c + 1)
                addRow(r - 1, c)
                addRow(r, c - 1)
            
            steps += 1
                    


                