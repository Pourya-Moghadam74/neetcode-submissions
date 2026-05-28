class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, currSum):
            if currSum == target:
                res.append(path[:])
                return

            if currSum > target:
                return
            
            if i >= len(nums):
                return
            
            path.append(nums[i])
            currSum += nums[i]
            dfs(i, currSum)
            currSum -= nums[i]
            path.pop()
            dfs(i + 1, currSum)

        dfs(0, 0)
        
        return res

            
