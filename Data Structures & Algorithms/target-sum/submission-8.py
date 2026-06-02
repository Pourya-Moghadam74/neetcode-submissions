class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = []

        def dfs(i, currSum):
            if i == len(nums):
                if currSum == target:
                    res.append(1)
                return

            if i > len(nums):
                return 
            
            dfs(i + 1, currSum + nums[i])
            dfs(i + 1, currSum - nums[i])
        
        dfs(0, 0)
        return len(res)