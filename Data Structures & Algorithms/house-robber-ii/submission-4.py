class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(arr):
            if len(arr) == 0:
                return 0
            
            if len(arr) == 1:
                return arr[0]

            dp = [arr[0], max(arr[0], arr[1])]
            for j in range(2, len(arr)):
                tmp = dp[1]
                dp[1] = max(dp[0] + arr[j], dp[1])
                dp[0] = tmp
            
            return dp[1]

        return max(helper(nums[:n - 1]), helper(nums[1 : n]))