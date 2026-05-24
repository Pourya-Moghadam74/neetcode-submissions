class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(i):

            if i == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
            dfs(i + 1)
        
            return res
        
        return dfs(0)