class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS = defaultdict(int)
        for ch in t:
            countS[ch] += 1
        
        l = 0
        window = {}
        res = ""
        resLen = float("inf")
        need, have = len(countS), 0

        for r in range(len(s)):
            right_ch = s[r]
            window[right_ch] = 1 + window.get(right_ch, 0)

            if right_ch not in countS:
                continue
            
            if countS[right_ch] == window[right_ch]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = s[l: r + 1]
                    resLen = r - l + 1
            
                left_ch = s[l]
                window[left_ch] -= 1

                if left_ch in countS and window[left_ch] < countS[left_ch]:
                    have -= 1

                l += 1

        return res