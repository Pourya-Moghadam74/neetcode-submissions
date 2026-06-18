class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for p, s in zip(position, speed):
            arr.append((p, s))

        arr.sort(reverse=True)
        fleet = []

        for p, s in arr:
            time = (target - p) / s
            if fleet and fleet[-1] >= time:
                continue
            
            else:
                fleet.append(time)
        
        return len(fleet)
