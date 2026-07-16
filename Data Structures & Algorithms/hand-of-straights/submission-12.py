class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for n in range(first, first + groupSize):
                if n not in count:
                    return False
                
                count[n] -= 1

                if count[n] == 0:
                    if n != minH[0]:
                        return False
                    
                    heapq.heappop(minH)
        
        return True