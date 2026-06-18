class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        for ch in s1:
            count[ch] += 1
        
        window = {}
        l = 0

        for r in range(len(s2)):
            right_ch = s2[r]
            window[right_ch] = 1 + window.get(right_ch, 0)

            if (r - l + 1) < len(s1):
                continue
            
            if count == window:
                return True
            
            left_ch = s2[l]
            window[left_ch] -= 1
            if window[left_ch] <= 0:
                del window[left_ch]
            l += 1

        return False