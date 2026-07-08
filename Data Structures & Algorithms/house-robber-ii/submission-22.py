class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            if len(nums) == 1:
                return nums[0]
            
            dp = [nums[0], max(nums[0], nums[1])]

            for i in range(2, len(nums)):
                tmp = dp[1]
                dp[1] = max(dp[0] + nums[i], dp[1])
                dp[0] = tmp
            
            return dp[1]
        
        return max(helper(nums[:-1]), helper(nums[1:]))