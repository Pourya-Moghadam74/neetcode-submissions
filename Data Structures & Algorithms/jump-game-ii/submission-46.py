class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        dp = [0] * (len(nums) - 1)

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                dp[i] = float('inf')
            
            else:
                end = min(len(nums) - 1, nums[i] + i)
                if end == len(nums) - 1:
                    dp[i] = 1
                
                else:
                    dp[i] = 1 + min(dp[i + 1: end + 1])
            

        return dp[0]