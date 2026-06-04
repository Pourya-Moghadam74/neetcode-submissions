class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = defaultdict(int)
        count[nums[0]] += 1
        count[-nums[0]] += 1

        for i in range(1, len(nums)):
            nextCount = defaultdict(int)
            for item in count:
                nextCount[item + nums[i]] += count[item]
                nextCount[item - nums[i]] += count[item]
            count = nextCount
        
        return count[target] if target in count else 0
