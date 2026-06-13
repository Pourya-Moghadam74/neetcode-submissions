class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        cache = {}

        def dfs(i, j):
            if i >= rows or j >= cols:
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            right = 1 + dfs(i, j + 1)
            down = 1 + dfs(i + 1, j)
            diag = 1 + dfs(i + 1, j + 1)

            cache[(i, j)] = min(right, down, diag) if matrix[i][j] != "0" else 0

            return cache[(i, j)]
        
        dfs(0, 0)

        return max(cache.values()) ** 2