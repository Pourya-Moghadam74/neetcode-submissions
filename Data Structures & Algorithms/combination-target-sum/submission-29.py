class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curSum, comb):
            if curSum == target:
                res.append(comb[:])
                return 
                
            if curSum > target:
                return
                
            if i >= len(nums):
                return
            
            dfs(i, curSum + nums[i], comb + [nums[i]])
            dfs(i + 1, curSum, comb)
        
        dfs(0, 0, [])

        return res