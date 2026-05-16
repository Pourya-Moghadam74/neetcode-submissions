class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []

        def dfs(i):

            if i >= len(nums):
                return res.append(path[:])
            
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
            dfs(i + 1)

            return res
        
        return dfs(0)