class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        resIdx = 0
        resLen = float("inf")

        l = 0
        window = {}
        need, have = len(count), 0

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if window[s[r]] == count[s[r]]:
                have += 1
            
            while need == have:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    resIdx = l
                
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                    if window[s[l]] == 0:
                        del window[s[l]]
                
                l += 1
        
        return s[resIdx: resIdx + resLen] if resLen != float("inf") else ""