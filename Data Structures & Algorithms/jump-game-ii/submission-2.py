class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        l, r = 0, 0
        end = 0
        while r < len(nums) - 1:
            
            for i in range(l, r + 1):
                end = max(end, nums[i] + i)

            l = r + 1
            r = end
            jump += 1
        
        return jump