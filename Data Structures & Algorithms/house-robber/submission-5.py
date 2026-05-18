class Solution:
    def rob(self, nums: List[int]) -> int:

        def dfs(i, cache):
            if i == len(nums) - 1:
                cache[i] = nums[i]
                return nums[i]
            
            if i >= len(nums):
                cache[i] = 0
                return 0
            
            if i in cache:
                return cache[i]
            
            count = max(dfs(i+1, cache), nums[i] + dfs(i+2, cache))
            
            if i not in cache:
                cache[i] = count
            
            return count
        
        return dfs(0, {})