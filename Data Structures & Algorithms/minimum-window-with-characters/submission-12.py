class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        for ch in t:
            count[ch] = 1 + count.get(ch, 0)
        
        l = 0
        window = {}
        res = ""
        resLen = float("inf")

        have, need = 0, len(count)

        for r in range(len(s)):
            rch = s[r]
            window[rch] = 1 + window.get(rch, 0)

            if rch in count and count[rch] == window[rch]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = s[l:r + 1]
                
                lch = s[l]
                window[lch] -= 1
                if lch in count and window[lch] < count[lch]:
                    have -= 1
                l += 1
        
        return res
