class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
            
        dp = [0] * n
        dp[n - 1] = 0
        dp[n - 2] = 1

        for i in range(n - 3, -1, -1):
            res = float('inf')
            for j in range(i + 1, min(n, nums[i] + i + 1)):
                res = min(res, dp[j])
            
            dp[i] = 1 + res
        
        return dp[0]