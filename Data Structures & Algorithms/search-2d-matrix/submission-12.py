class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l, r = 0, (ROWS * COLS) - 1

        while l <= r:
            m = (l + r) // 2
            mid = matrix[m // COLS][m % COLS]
            if mid == target:
                return True
            
            elif mid > target:
                r = m - 1
            
            else:
                l = m + 1
        
        return False

