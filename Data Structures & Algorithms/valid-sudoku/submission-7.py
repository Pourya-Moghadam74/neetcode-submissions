class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                boxId = (r // 3) * 3 + (c // 3)
                cell = board[r][c]
                if cell == ".":
                    continue
                    
                if cell in rows[r] or cell in cols[c] or cell in boxes[boxId]:
                    return False
                
                rows[r].add(cell)
                cols[c].add(cell)
                boxes[boxId].add(cell)
        

        return True