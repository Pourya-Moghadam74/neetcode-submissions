class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = defaultdict(int)
        for ch in t:
            count[ch] += 1
        
        have, need = 0, len(count)
        window = {}
        l = 0
        res, resLen = "", float("inf")
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in count and count[s[r]] == window[s[r]]:
                have += 1
            
            while need == have:
                if resLen > (r - l + 1):
                    res = s[l: r + 1]
                    resLen = (r - l + 1)

                window[s[l]] -= 1
                if s[l] in count and count[s[l]] > window[s[l]]:
                    have -= 1
                
                l += 1
        
        return res