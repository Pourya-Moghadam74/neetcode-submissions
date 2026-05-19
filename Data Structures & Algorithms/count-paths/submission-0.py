class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * m

        for row in range(n - 1, -1, -1):
            currRow = [0] * m
            currRow[-1] = 1

            for col in range(m - 2, -1, -1):
                currRow[col] = prevRow[col] + currRow[col+1]
            
            prevRow = currRow
        
        return currRow[0]
