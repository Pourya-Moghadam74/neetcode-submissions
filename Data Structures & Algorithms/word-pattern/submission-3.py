class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map1 = {}
        map2 = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
            
        for c1, c2 in zip(pattern, s):
            if c1 not in map1:
                map1[c1] = c2
            
            elif map1[c1] != c2:
                return False
            
            if c2 not in map2:
                map2[c2] = c1
            elif map2[c2] != c1:
                return False

        return True