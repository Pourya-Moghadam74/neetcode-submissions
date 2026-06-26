class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh, mins = 0, 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
        

        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        (nr, nc) in visited or
                        grid[nr][nc] == 0
                    ):
                        continue
                    
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    fresh -= 1
            mins += 1

        return mins if fresh == 0 else -1