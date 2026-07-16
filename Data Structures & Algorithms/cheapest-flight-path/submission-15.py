class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tempPrice = prices[:]

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                
                if prices[s] + p < tempPrice[d]:
                    tempPrice[d] = prices[s] + p
                
            prices = tempPrice
        
        return prices[dst] if prices[dst] != float("inf") else -1