class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        cache = {}
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(r, c):
            if r >= rows or c >= cols:
                return 0
            
            if (r, c) in cache:
                return cache[(r, c)]
                
            right = dfs(r, c + 1)
            down = dfs(r + 1, c)
            diag = dfs(r + 1, c + 1)

            if matrix[r][c] == "0":
                cache[(r, c)] = 0
            
            else:
                cache[(r, c)] = 1 + min(right, down, diag)

            return cache[(r, c)]
        dfs(0, 0)
        return max(cache.values()) ** 2

            
