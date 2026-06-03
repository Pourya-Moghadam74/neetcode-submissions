class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)

        def dfs(i, currSum):
            if i >= n:
                return
            
            if currSum > target:
                return
            
            if currSum == target:
                res.append(path[:])
                return
            
            path.append(nums[i])
            dfs(i, currSum + nums[i])
            path.pop()
            dfs(i + 1, currSum)

        dfs(0, 0)

        return res
