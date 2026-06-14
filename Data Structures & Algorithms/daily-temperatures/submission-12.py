class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #temp, day
        res = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                t2, i2 = stack.pop()
                res[i2] = i - i2
            
            stack.append((t, i))
        
        return res
            