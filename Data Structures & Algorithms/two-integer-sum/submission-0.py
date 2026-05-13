class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i in range(len(nums)):
            dist = target - nums[i]

            if dist in values:
                return [values[dist], i]
            
            else:
                values[nums[i]] = i
            
        