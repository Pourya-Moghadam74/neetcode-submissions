class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n - 2, -1, -1):
            tmp = 0
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    tmp = max(tmp,dp[j])
            dp[i] = 1 + tmp
        return max(dp)