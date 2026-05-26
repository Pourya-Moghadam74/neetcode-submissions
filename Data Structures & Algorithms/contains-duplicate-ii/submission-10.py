class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        values = {}

        for i in range(len(nums)):
            if nums[i] in values and i - values[nums[i]] <= k:
                return True
            
            values[nums[i]] = i
        

        return False