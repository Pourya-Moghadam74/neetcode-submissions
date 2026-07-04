class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def helper(arr):
            n = len(arr)
            if n == 0:
                return 0
            
            if n == 1:
                return arr[0]
            
            dp = [arr[0], max(arr[0], arr[1])]

            for i in range(2, n):
                tmp = dp[1]
                dp[1] = max(dp[0] + arr[i], dp[1])
                dp[0] = tmp
            
            return dp[1]
        

        return max(helper(nums[:-1]), helper(nums[1:]))