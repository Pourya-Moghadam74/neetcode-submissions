class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top, bottom = 0, rows - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] == target:
                return True
            
            elif matrix[mid][0] > target:
                bottom = mid - 1
            
            else:
                top = mid + 1
            
        row = bottom
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            val = matrix[row][mid]
            if val == target:
                return True
            
            elif val > target:
                r = mid - 1
            
            else:
                l = mid + 1

        return False
            