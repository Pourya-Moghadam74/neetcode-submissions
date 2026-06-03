class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = [[]]

        for num in nums:
            nextPerm = []
            for p in perm:
                for j in range(len(p) + 1):
                    pCopy = p[:]
                    pCopy.insert(j, num)
                    nextPerm.append(pCopy)
            perm = nextPerm
        
        return perm

                