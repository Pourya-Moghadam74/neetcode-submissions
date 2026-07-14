class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.preSum = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        for r in range(ROWS):
            total = 0
            for c in range(COLS):
                total += matrix[r][c]
                self.preSum[r][c] += total
                if r > 0:
                    self.preSum[r][c] += self.preSum[r - 1][c]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 > 0:
            above = self.preSum[row1 - 1][col2]
        else:
            above = 0
        
        if col1 > 0:
            left = self.preSum[row2][col1 - 1]
        else:
            left = 0
        
        if row1 > 0 and col1 > 0:
            topLeft = self.preSum[row1 - 1][col1 - 1]
        else:
            topLeft = 0
        
        main = self.preSum[row2][col2]
        return main - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)