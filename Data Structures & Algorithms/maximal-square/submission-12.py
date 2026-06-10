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

            down = 1 + dfs(i + 1, j)
            right = 1 + dfs(i, j + 1)
            diag = 1 + dfs(i + 1, j + 1)
            
            if matrix[i][j] == "0":
                cache[(i, j)] = 0
            else:
                cache[(i, j)] = min(down, right, diag)

            return cache[(i, j)]
        
        dfs(0, 0)

        return max(cache.values()) ** 2
