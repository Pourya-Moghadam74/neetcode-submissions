class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(open, close):
            if open == close == n:
                res.append("".join(path))
                return
            
            if open < close or open > n or close > n:
                return
            
            path.append("(")
            dfs(open + 1, close)
            path.pop()
            path.append(")")
            dfs(open, close + 1)
            path.pop()
        
        dfs(0, 0)

        return res