class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n - 2, -1, -1):
            if nums[i] == 0:
                dp[i] = float('inf')
            
            else:
                end = min(nums[i] + i, n - 1)
                if end == n - 1:
                    dp[i] = 1
                else:
                    tmp = float('inf')
                    for j in range(i + 1, end + 1):
                        tmp = min(dp[j], tmp)
                    
                    dp[i] = 1 + tmp
            

        return dp[0]