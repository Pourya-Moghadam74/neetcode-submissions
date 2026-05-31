class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False

            end = nums[i] + i
            if end >= len(nums) - 1:
                return True
            
            for j in range(i + 1, nums[i] + i + 1):
                end = nums[j] + j
                if end >= len(nums) - 1:
                    return True
                
                farthest = max(farthest, nums[j] + j)
            
            if farthest >= len(nums) - 1:
                return True
            
        return False