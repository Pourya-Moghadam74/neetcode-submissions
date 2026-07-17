class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        count = {}
        
        for idx, n in enumerate(numbers):
            diff = target - n
            if diff in count:
                return [count[diff] + 1, idx + 1]
            
            count[n] = idx
        
        
        