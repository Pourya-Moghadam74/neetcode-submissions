class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def dfs(i):
            if i >= len(s):
                return True

            if i in cache:
                return cache[i]

            for word in wordDict:
                length = len(word)
                if s[i:i + length] == word:
                    if dfs(i + length):
                        cache[i] = True
                        return True
                    else:
                        cache[i] = False
            
            return False
        
        return dfs(0)