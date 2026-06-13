class Solution:
    def isValid(self, s: str) -> bool:
        closToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for item in s:
            if item in "([{":
                stack.append(item)
            
            elif not stack or stack.pop() != closToOpen[item]:
                return False
        
        return True if not stack else False