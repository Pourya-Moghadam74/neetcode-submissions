class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        fleet = []

        for p, s in cars:
            time = (target - p) / s

            if fleet and fleet[-1] >= time:
                continue
            
            else:
                fleet.append(time)
        
        return len(fleet)
