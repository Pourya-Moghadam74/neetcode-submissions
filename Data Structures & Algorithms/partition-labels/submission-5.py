class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indices = {}
        for idx, ch in enumerate(s):
            indices[ch] = idx
        
        farthest = 0
        l = 0
        res = []

        for i in range(len(s)):
            farthest = max(farthest, indices[s[i]])
            if i == farthest:
                res.append(i - l + 1)
                l = i + 1
            
        return res