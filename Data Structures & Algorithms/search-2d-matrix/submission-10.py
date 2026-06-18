class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, cols * rows - 1

        while l <= r:
            m = (l + r) // 2
            val = matrix[m // cols][m % cols]
            if val == target:
                return True
            
            elif val > target:
                r = m - 1
            
            else:
                l = m + 1
        
        return False