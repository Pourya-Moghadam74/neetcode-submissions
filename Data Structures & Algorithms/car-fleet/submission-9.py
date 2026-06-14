class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for p, s in zip(position, speed):
            arr.append((p, s))
        
        arr.sort(reverse=True)
        stack = []
        for p, s in arr:
            time = (target - p) / s

            if stack and time <= stack[-1]:
                continue
            
            else:
                stack.append(time)
        
        return len(stack)