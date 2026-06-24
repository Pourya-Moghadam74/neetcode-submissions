class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for s in s1:
            count[s] = 1 + count.get(s, 0)
        
        l = 0
        window = {}

        for r in range(len(s2)):
            window[s2[r]] = 1 + window.get(s2[r], 0)

            if (r - l + 1) < len(s1):
                continue
            
            if window == count:
                return True
            
            window[s2[l]] -= 1
            if window[s2[l]] <= 0:
                del window[s2[l]]
            
            l += 1
        
        return False
