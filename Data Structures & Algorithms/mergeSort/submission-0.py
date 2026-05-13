# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)

        def merge(a, b):
            res = []
            i, j = 0, 0

            while i < len(a) and j < len(b):
                if a[i].key <= b[j].key:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1

            if i < len(a):
                res = res + a[i:]   
            
            if j < len(b):
                res = res + b[j:]
            
            return res


        if n <= 1:
            return pairs
        
        mid = n // 2
        a = self.mergeSort(pairs[:mid])
        b = self.mergeSort(pairs[mid:])

        return merge(a, b)

