class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 1
        n = len(nums)
        if n == 1:
            return 0
        
        l, r = 1, nums[0]

        while r < n - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            
            l = r + 1
            r = farthest
            jump += 1
        
        return jump
        

                
        

        
