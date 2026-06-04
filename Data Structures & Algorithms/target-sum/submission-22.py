class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = {}
        count[nums[0]] = count.get(nums[0], 0) + 1
        count[-nums[0]] = count.get(-nums[0], 0) + 1

        for i in range(1, len(nums)):
            nextCount = {}

            for total in count:
                nextCount[total + nums[i]] = nextCount.get(total + nums[i], 0) + count[total]
                nextCount[total - nums[i]] = nextCount.get(total - nums[i], 0) + count[total]

            count = nextCount

        return count.get(target, 0)