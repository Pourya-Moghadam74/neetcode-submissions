class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2:
            return False
        
        target = totalSum // 2

        dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]

        for i in range(target + 1):
            dp[0][i] = True if i == nums[0] else False
        
        for r in range(1, len(nums)):
            for c in range(target + 1):
                take = 0
                if c >= nums[r]:
                    take = dp[r - 1][c - nums[r]]
                
                skip = dp[r - 1][c]
                dp[r][c] = take or skip
            
        return dp[-1][-1]