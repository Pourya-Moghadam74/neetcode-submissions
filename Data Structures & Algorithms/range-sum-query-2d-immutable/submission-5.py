class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for row in range(len(matrix)):
            total = 0
            for col in range(len(matrix[0])):
                total += matrix[row][col]
                self.prefix[row][col] = total
                if row > 0:
                    self.prefix[row][col] += self.prefix[row - 1][col]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.prefix[row2][col2]
        above, left, topLeft = 0, 0, 0
        if row1 - 1 >= 0:
            above = self.prefix[row1 - 1][col2]
        if col1 - 1 >= 0:
            left = self.prefix[row2][col1 - 1]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            topLeft = self.prefix[row1 - 1][col1 - 1]

        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)