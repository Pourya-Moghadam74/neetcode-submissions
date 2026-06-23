class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        r = 0
        while r < len(s):
            if s[r] != "#":
                r += 1
                continue
            
            length = int(s[l:r])
            res.append(s[r + 1: r + 1 + length])
            l = r + 1 + length
            r = r + 1 + length
        
        return res