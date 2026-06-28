class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            end = min(nums[i] + i, len(nums) - 1)
            if end == len(nums) - 1:
                dp[i] = 1
            
            elif nums[i] == 0:
                dp[i] = float("inf")

            else:
                dp[i] = 1 + min(dp[i + 1 : end + 1])
        
        return dp[0]