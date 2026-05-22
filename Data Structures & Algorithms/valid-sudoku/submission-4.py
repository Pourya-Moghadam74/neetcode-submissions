class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(len(board))]
        cols = [[] for _ in range(len(board[0]))]
        boxes = [[] for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]
                if value == '.':
                    continue
                box_id = (row//3) * 3 + (col//3)

                if value not in rows[row] and value not in cols[col] and value not in boxes[box_id]:
                    rows[row].append(value)
                    cols[col].append(value)
                    boxes[box_id].append(value)
                
                else:
                    return False
        
        return True