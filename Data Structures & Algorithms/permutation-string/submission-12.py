class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for s in s1:
            count[s] = 1 + count.get(s, 0)
        
        count2 = {}
        l = 0
        for r in range(len(s2)):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            while (r - l + 1) > len(s1):
                count2[s2[l]] -= 1
                if count2[s2[l]] <= 0:
                    del count2[s2[l]]
                
                l += 1
            
            if count2 == count:
                return True
        
        return False

