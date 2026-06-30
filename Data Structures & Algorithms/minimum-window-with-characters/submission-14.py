class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        for ch in t:
            count[ch] = 1 + count.get(ch, 0)
        
        res = ""
        resLen = float("inf")
        window = {}
        l = 0
        need, have = len(count), 0

        for r in range(len(s)):
            rCh = s[r]
            window[rCh] = 1 + window.get(rCh, 0)

            if rCh in count and window[rCh] == count[rCh]:
                have += 1
            
            while need == have:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = s[l: r + 1]
                
                lCh = s[l]
                window[lCh] -= 1

                if lCh in count and window[lCh] < count[lCh]:
                    have -= 1
                    
                if window[lCh] <= 0:
                    del window[lCh]
                
                l += 1
        
        return res
