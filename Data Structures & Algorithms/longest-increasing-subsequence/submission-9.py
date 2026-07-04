class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            tmp = 0
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    if dp[j] > tmp:
                        tmp = dp[j]
            
            dp[i] = 1 + tmp

        return max(dp)