class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        values = {}
        values[nums[0]] = values.get(nums[0], 0) + 1
        values[-nums[0]] = values.get(-nums[0], 0) + 1
        
        for i in range(1, len(nums)):
            nextValues = {}
            for t in values:
                count = values[t]
                nextValues[t + nums[i]] = nextValues.get(t + nums[i], 0) + count
                nextValues[t - nums[i]] = nextValues.get(t - nums[i], 0) + count

            values = nextValues
        
        return values.get(target, 0)