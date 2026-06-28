class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        firstRowZero = False
        firstColZero = False
        for i in range(COLS):
            if matrix[0][i] == 0:
                firstRowZero = True
                break
        
        for i in range(ROWS):
            if matrix[i][0] == 0:
                firstColZero = True
                break
        

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, ROWS):
            if matrix[r][0] == 0:
                for c in range(COLS):
                    matrix[r][c] = 0
        
        for c in range(1, COLS):
            if matrix[0][c] == 0:
                for r in range(ROWS):
                    matrix[r][c] = 0
        
        if firstRowZero:
            matrix[0][:] = [0] * COLS
        
        if firstColZero:
            for r in range(ROWS):
                matrix[r][0] = 0
        