class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = [[]]

        for num in nums:
            nextPerm = []
            for p in perm:
                for i in range(len(p) + 1):
                    pCopy = p[:]
                    pCopy.insert(i, num)
                    nextPerm.append(pCopy)
                
                perm = nextPerm
        
        return perm