class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def capture(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != "O" or
                (r, c) in visited
            ):
                return
            
            board[r][c] = "T"
            visited.add((r, c))

            capture(r + 1, c)
            capture(r, c + 1)
            capture(r - 1, c)
            capture(r, c - 1)

        
        for r in range(ROWS):
            capture(r, 0)
            capture(r, COLS - 1)

        for c in range(COLS):
            capture(0, c)
            capture(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
