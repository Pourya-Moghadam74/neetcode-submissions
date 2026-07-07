class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        starStack = []

        for i, ch in enumerate(s):
            if ch == ")":
                if stack:
                    stack.pop()
                
                elif starStack:
                    starStack.pop()
            
                else:
                    return False
            
            elif ch == "(":
                stack.append(i)
            
            elif ch == "*":
                starStack.append(i)
        
        if len(stack) > len(starStack):
            return False
        
        if len(stack) == 0:
            return True

        while stack and starStack:
            a, b = stack.pop(), starStack.pop()
            if b < a:
                return False
        
        return True