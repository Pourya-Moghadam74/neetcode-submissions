class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = {}

        def dfs(i, open, close):
            if i >= len(s):
                if open == close:
                    return True
                return False
            
            if open < close:
                return False

            if (i, open, close) in cache:
                return cache[(i, open, close)]    

            if s[i] == "(":
                cache[(i, open, close)] = dfs(i + 1, open + 1, close)
                return cache[(i, open, close)]
            
            if s[i] == ")":
                cache[(i, open, close)] = dfs(i + 1, open, close + 1)
                return cache[(i, open, close)]
            
            res = (
                dfs(i + 1, open, close) or
                dfs(i + 1, open + 1, close) or
                dfs(i + 1, open, close + 1)
            )
            cache[(i, open, close)] = res
            return res

        return dfs(0, 0, 0)