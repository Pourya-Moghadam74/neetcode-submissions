class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        resIdx = 0
        resLen = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if (j - i) <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if resLen < (j - i + 1):
                            resLen = j - i + 1
                            resIdx = i

        return s[resIdx:resIdx + resLen]
