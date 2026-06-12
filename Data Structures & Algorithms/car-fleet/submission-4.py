class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = [] #time

        for i in range(len(pair)):
            time = (target - pair[i][0]) / pair[i][1]
            if stack and time <= stack[-1]:
                continue
            
            else:
                stack.append(time)
        
        return len(stack)