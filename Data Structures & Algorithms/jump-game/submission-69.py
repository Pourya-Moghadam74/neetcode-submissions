class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            end = min(len(nums) - 1, nums[i] + i)
            dp[i] = any(dp[i + 1: end + 1])
        
        return dp[0]