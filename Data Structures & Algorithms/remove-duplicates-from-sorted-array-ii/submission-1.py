class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer = 2
        i = 2

        while i < len(nums):
            if nums[i] != nums[writer - 2]:
                nums[writer] = nums[i]
                writer += 1
            
            i += 1

        return writer