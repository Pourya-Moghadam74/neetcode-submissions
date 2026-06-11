class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        minHeap = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        

        for num, total in count.items():
            minHeap.append((total, num))
        
        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        res = []
        for item in minHeap:
            res.append(item[1])

        return res
