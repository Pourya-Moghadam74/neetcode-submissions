class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]

            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + dfs(i - 1, j - 1)
                return cache[(i, j)]
            
            cache[(i, j)] = max(dfs(i - 1, j), dfs(i, j - 1))
            return cache[(i, j)]
        
        return dfs(len(text1) - 1, len(text2) - 1)
