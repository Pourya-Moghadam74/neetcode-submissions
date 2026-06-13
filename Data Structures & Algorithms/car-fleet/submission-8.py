class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        stack = []

        for p, s in zip(position, speed):
            arr.append((p, s))
        
        arr.sort(reverse=True)

        for p, s in arr:
            time = (target - p) / s
            if stack and stack[-1] >= time:
                continue
            
            else:
                stack.append(time)
        

        return len(stack)
