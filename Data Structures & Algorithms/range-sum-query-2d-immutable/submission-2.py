class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0 for _ in  range(cols)] for _ in range(rows)]
        for row in range(rows):
            total = 0
            for col in range(cols):
                total += matrix[row][col]
                self.prefix[row][col] = total
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            if col1 > 0:
                res += self.prefix[i][col2] - self.prefix[i][col1 - 1]
            else:
                res += self.prefix[i][col2]

        return res
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)