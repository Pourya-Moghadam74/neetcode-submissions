class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(i1, i2):
            if len(word1[i1:]) == 0 and len(word2[i2:]) == 0:
                return 0

            if len(word1[i1:]) == 0 and len(word2[i2:]) != 0:
                return len(word2[i2:])
            
            if len(word1[i1:]) != 0 and len(word2[i2:]) == 0:
                return len(word1[i1:])
        
            if (i1, i2) in cache:
                return cache[(i1, i2)]

            if word1[i1] == word2[i2]:
                cache[(i1, i2)] = dfs(i1 + 1, i2 + 1)
                return cache[(i1, i2)]
            
            else:
                replace = 1 + dfs(i1 + 1, i2 + 1)
                delete = 1 + dfs(i1 + 1, i2)
                insert = 1 + dfs(i1, i2 + 1)

                cache[(i1, i2)] = min(replace, delete, insert)
                return cache[(i1, i2)]
        
        return dfs(0, 0)