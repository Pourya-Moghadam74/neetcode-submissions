class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            
            end = min(nums[i] + i, len(nums) - 1)
            for j in range(i + 1, end + 1):
                farthest = max(farthest, nums[j] + j)
                if farthest == len(nums) - 1:
                    return True
        
        return True