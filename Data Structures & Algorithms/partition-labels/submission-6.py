class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        count = {}
        for i, ch in enumerate(s):
            count[ch] = i
        
        farthest = 0
        l = 0
        for r in range(len(s)):
            farthest = max(farthest, count[s[r]])
            if farthest == r:
                res.append(r - l + 1)
                l = r + 1
            
        return res
