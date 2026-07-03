class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            if len(arr) < 2:
                return arr[0]
            
            dp = [arr[0], max(arr[0], arr[1])]

            for i in range(2, len(arr)):
                tmp = dp[1]
                dp[1] = max(arr[i] + dp[0], dp[1])
                dp[0] = tmp
            
            return dp[1]

        return max(helper(nums[:-1]), helper(nums[1:]))
