class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        cache = {}

        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]           
        
            right = dfs(i, j + 1)
            down = dfs(i + 1, j)
            diag = dfs(i + 1, j + 1)

            if matrix[i][j] == "0":
                cache[(i, j)] = 0

            else:
                cache[(i, j)] = 1 + min(right, down, diag)
        
            return cache[(i, j)]
        
        dfs(0, 0)

        return max(cache.values()) ** 2
