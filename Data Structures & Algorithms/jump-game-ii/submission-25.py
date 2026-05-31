class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n - 2, -1, -1):
            end = nums[i] + i
            if end >= n - 1:
                dp[i] = 1
            else:
                res = float('inf')
                for j in range(i + 1, end + 1):
                    res = min(res, dp[j])
                dp[i] = 1 + res
            
        return dp[0]
