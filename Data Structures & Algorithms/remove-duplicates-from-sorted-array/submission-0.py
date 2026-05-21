class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer = 0

        for i in range(len(nums)):
            if i < 1 or nums[i] != nums[i - 1]:
                nums[writer] = nums[i]
                writer += 1        
            
        return writer