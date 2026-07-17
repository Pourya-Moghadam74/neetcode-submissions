class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        resIdx = 0
        resLen = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if resLen < j - i + 1:
                            resLen = j - i + 1
                            resIdx = i
                        
        return s[resIdx: resIdx + resLen]