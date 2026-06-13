class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        for ch in s:
            if ch in closeToOpen:
                if not stack or stack[-1] != closeToOpen[ch]:
                    return False
                
                else:
                    stack.pop()
            
            else:
                stack.append(ch)
        
        return True if not stack else False