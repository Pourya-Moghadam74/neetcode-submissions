class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        arr = [(p, s) for p, s in zip(position, speed)]
        arr.sort(reverse=True)

        for p, s in arr:
            time = (target - p) / s

            if fleet and fleet[-1] >= time:
                continue
            
            else:
                fleet.append(time)
        

        return len(fleet)