class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def dfs():
            token = tokens.pop()
            if token not in "+*-/":
                return int(token)
            
            right = dfs()
            left = dfs()

            if token == "+":
                return left + right
            
            elif token == "-":
                return left - right
            
            elif token == "*":
                return left * right
            
            else:
                return int(left / right)
            
        
        return dfs()