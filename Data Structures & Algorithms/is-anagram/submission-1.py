class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        values = {}

        if len(s) != len(t):
            return False
        
        for ch in s:
            if ch not in values:
                values[ch] = 1
            else:
                values[ch] += 1
        
        for ch in t:
            if ch in values:
                values[ch] -= 1
                if values[ch] < 0:
                    return False
            else:
                return False
            
        
        return True