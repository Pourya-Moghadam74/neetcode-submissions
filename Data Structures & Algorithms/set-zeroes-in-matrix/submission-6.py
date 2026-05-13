class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_zeros = any(matrix[0][i] == 0 for i in range(cols))
        first_col_zeros = any(matrix[i][0] == 0 for i in range(rows))

        for row in range(1, rows):
            for col in range(1,cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, rows):
            if matrix[row][0] == 0:
                for i in range(cols):
                    matrix[row][i] = 0
        
        for col in range(1, cols):
            if matrix[0][col] == 0:
                for i in range(rows):
                    matrix[i][col] = 0
            
        if first_row_zeros:
            for i in range(cols):
                matrix[0][i] = 0
        
        if first_col_zeros:
            for i in range(rows):
                matrix[i][0] = 0
    

        