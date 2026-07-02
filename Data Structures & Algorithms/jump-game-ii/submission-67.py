class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n - 2, -1, -1):
            end = min(nums[i] + i, n - 1)
            ans = float("inf")
            for j in range(i + 1, end + 1):
                ans = min(ans, dp[j])
            dp[i] = 1 + ans

        return dp[0]