class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        perm = [[]]


        for n in nums:
            nextPerm = []
            for p in perm:
                for j in range(len(p) + 1):
                    pCopy = p[:]
                    pCopy.insert(j, n)
                    if pCopy not in nextPerm:
                        nextPerm.append(pCopy)
            perm = nextPerm

    
        return perm
                