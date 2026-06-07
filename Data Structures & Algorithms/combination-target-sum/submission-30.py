class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(i, curSum):
            if curSum == target:
                res.append(comb[:])
                return
            
            if i >= len(nums):
                return
            
            if curSum > target:
                return
            
            comb.append(nums[i])
            dfs(i, curSum + nums[i])
            comb.pop()
            dfs(i + 1, curSum)
        
        dfs(0, 0)

        return res