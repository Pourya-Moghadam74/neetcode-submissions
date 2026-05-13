class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i >= 1 and nums[i-1] == a:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:

                threesum = a + nums[left] + nums[right]

                if threesum > 0:
                    right -= 1
                
                elif threesum < 0:
                    left += 1
                
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
        return res
