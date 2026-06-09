class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        cache = {}

        def dfs(i, j):
            if i >= m and j >= n:
                return 0
            
            if i >= m:
                return len(word2[j:])
            
            if j >= n:
                return len(word1[i:])
            
            if (i, j) in cache:
                return cache[(i, j)]

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
                
            replace = 1 + dfs(i + 1, j + 1)
            insert = 1 + dfs(i, j + 1)
            delete = 1 + dfs(j + 1, i)

            cache[(i, j)] = min(replace, insert, delete)
            return cache[(i, j)]
        
        return dfs(0, 0)