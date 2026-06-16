class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.prefix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for r in range(self.rows):
            total = 0
            for c in range(self.cols):
                total += matrix[r][c]
                self.prefix[r][c] = total
                if r > 0:
                    self.prefix[r][c] += self.prefix[r - 1][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        above = 0
        if row1 > 0:
            above = self.prefix[row1 - 1][col2]
        left = 0
        if col1 > 0:
            left = self.prefix[row2][col1 - 1]
        topLeft = 0
        if col1 > 0 and row1 > 0:
            topLeft = self.prefix[row1 - 1][col1 - 1]
        
        return self.prefix[row2][col2] - above - left + topLeft