class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        steps = 0
        while q:
            steps += 1
            size = len(q)
            for i in range(size):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        grid[nr][nc] != INF
                    ):
                        continue
                    else:
                        q.append((nr, nc))
                        grid[nr][nc] = steps
        

                    
