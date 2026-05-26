class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

        for c1, c2 in zip(s, t):
            if c1 not in map1:
                map1[c1] = c2
            
            elif map1[c1] != c2:
                return False
            
            if c2 not in map2:
                map2[c2] = c1
            
            elif map2[c2] != c1:
                return False
        
        return True