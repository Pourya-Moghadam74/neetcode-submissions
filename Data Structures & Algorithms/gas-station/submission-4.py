class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        i = 0
        if sum(gas) < sum(cost):
            return -1
        
        while i < len(gas):
            gain = gas[i] - cost[i]
            tank += gain

            if tank >= 0:
                i += 1
            
            else:
                start = i + 1
                tank = 0
                i += 1

        return start
