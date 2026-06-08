class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            end = min(nums[i] + i, len(nums) - 1)
            if nums[i] == 0:
                dp[i] = False
            
            if end == len(nums) - 1:
                dp[i] = True
        
            dp[i] = any(dp[i + 1: end + 1])

        return dp[0]