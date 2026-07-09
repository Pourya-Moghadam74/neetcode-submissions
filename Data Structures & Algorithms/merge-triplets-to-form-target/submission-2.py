class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        arr = [float("-inf"), float("-inf"), float("-inf")]
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            arr = [max(arr[0], t[0]), max(arr[1], t[1]), max(arr[2], t[2])]
        
        return arr == target
