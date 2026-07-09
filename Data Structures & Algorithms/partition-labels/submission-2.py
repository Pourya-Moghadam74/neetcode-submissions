class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indices = {}
        for idx, ch in enumerate(s):
            indices[ch] = idx
        
        farthest = -1
        l = 0
        res = []
        for i in range(len(s)):
            farthest = max(indices[s[i]], farthest)

            if i == farthest:
                res.append(i - l + 1)
                l = i + 1
        
        return res
