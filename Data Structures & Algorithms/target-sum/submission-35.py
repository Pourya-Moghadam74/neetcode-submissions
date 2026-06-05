class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = defaultdict(int)
        count[nums[0]] += 1
        count[-nums[0]] += 1

        for i in range(1, len(nums)):
            nextCount = defaultdict(int)
            for total, count in count.items():
                nextCount[total + nums[i]] += count
                nextCount[total - nums[i]] += count
            
            count = nextCount
        
        return count[target] if target in count else 0
