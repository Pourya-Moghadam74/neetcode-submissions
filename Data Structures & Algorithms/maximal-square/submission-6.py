class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        cache = {}

        def dfs(r, c):
            if r >= m or c >= n:
                return 0
            
            if (r, c) in cache:
                return cache[(r, c)]

            right = dfs(r, c + 1)
            down = dfs(r + 1, c)
            diag = dfs(r + 1, c + 1)
            cache[(r, c)] = 0
            if matrix[r][c] == "1":
                cache[(r, c)] = 1 + min(right, down, diag)       

            return cache[(r, c)]
        
        dfs(0, 0)
        return max(cache.values()) ** 2