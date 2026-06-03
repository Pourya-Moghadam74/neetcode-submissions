class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True
        
        dp = [False] * n
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            end = min(n - 1, nums[i] + i)
            
            if end == n - 1:
                dp[i] = True
            
            else:
                dp[i] = any(dp[i + 1: end + 1])
        
        return dp[0]