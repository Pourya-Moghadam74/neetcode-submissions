class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for ch in s:
            if ch in ["(", "{", "["]:
                stack.append(ch)
            
            elif ch in closeToOpen:
                if not stack:
                    return False
                
                elif closeToOpen[ch] == stack.pop():
                    continue
                else:
                    return False
        
        return True if not stack else False