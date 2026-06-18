class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        countS2 = {}
        have, need = 0, 0
        l = 0

        for item in s1:
            count[item] = 1 + count.get(item, 0)

        for r in range(len(s2)):
            ch = s2[r]
            countS2[ch] = 1 + countS2.get(ch, 0)

            if (r - l + 1) < len(s1):
                continue
            
            if countS2 == count:
                return True
            
            ch_l = s2[l]
            countS2[ch_l] -= 1
            if countS2[ch_l] == 0:
                del countS2[ch_l]

            l += 1
            
        return False
            

            

