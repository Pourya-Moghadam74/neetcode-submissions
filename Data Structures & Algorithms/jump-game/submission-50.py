class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        if n == 1:
            return True
        
        for i in range(n - 2, -1, -1):
            end = min(nums[i] + i, n - 1)
            if end == n - 1:
                dp[i] = True
            
            else:
                dp[i] = any(dp[i + 1: end + 1])
            
        return dp[0]