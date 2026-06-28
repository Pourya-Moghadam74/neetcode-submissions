class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def addCell(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                board[r][c] != "O"
            ):
                return
            
            visited.add((r, c))
            q.append((r, c))
            board[r][c] = "Marked"

        for c in range(COLS):
            if board[0][c] == "O":
                q.append((0, c))
            
            if board[ROWS - 1][c] == "O":
                q.append((ROWS - 1, c))
            
        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r, 0))
            
            if board[r][COLS - 1] == "O":
                q.append((r, COLS - 1))
        
        while q:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                addCell(r + 1, c)
                addCell(r, c + 1)
                addCell(r - 1, c)
                addCell(r, c - 1)

        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "Marked":
                    board[r][c] = "O"
        






