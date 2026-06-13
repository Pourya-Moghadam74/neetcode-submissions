class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perm = self.permute(nums[1:])
        nextPerm = []
        for p in perm:
            for i in range(len(p) + 1):
                pCopy = p[:]
                pCopy.insert(i, nums[0])
                nextPerm.append(pCopy)
        
        return nextPerm

