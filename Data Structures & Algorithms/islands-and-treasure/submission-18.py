class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        steps = 0
        while q:
            steps += 1
            size = len(q)
            for i in range(size):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        (nr, nc) in visited or
                        grid[nr][nc] == -1
                    ):
                        continue
                    
                    grid[nr][nc] = steps
                    q.append((nr, nc))
                    visited.add((nr, nc))
        

