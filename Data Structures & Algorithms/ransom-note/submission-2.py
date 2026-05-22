class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        values = {}

        for ch in magazine:
            values[ch] = 1 + values.get(ch, 0)

        for ch in ransomNote:
            if ch not in values:
                return False
            elif values[ch] <= 0:
                return False
            else:
                values[ch] -= 1
            
        
        return True