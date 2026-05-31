class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        values = set()
        res = 0

        for r in range(len(s)):
            while l < r and s[r] in values:
                values.remove(s[l])
                l += 1
            values.add(s[r])
            res = max(res, r - l + 1)
        
        return res
