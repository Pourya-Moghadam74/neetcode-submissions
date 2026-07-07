class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indices = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in indices:
                indices[s[i]] = i
        
        farthest = 0
        l = 0
        res = []

        for r in range(len(s)):
            farthest = max(indices[s[r]], farthest)
            if farthest == r:
                res.append(r - l + 1)
                l = r + 1
        
        return res


