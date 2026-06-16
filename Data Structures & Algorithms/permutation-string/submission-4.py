class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for s in s1:
            count[s] = 1 + count.get(s, 0)
        
        l = 0

        for i in range(len(s2) - len(s1) + 1):
            count2 = {}
            for j in range(i, i + len(s1)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
            
            if count2 == count:
                return True
            
        return False

