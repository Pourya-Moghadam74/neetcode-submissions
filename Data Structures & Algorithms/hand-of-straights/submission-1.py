class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            n = heap[0]
            
            for i in range(n, n + groupSize):
                if i not in count:
                    return False
                
                count[i] -= 1
                if count[i] == 0:
                    if heap[0] != i:
                        return False
                    
                    heapq.heappop(heap)
                
        
        return True


