class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        maxHeap = [cnt for cnt in count.values()]
        heapq.heapify_max(maxHeap)
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop_max(maxHeap)
                if cnt - 1 > 0:
                    q.append((time + n, cnt - 1))
                
            if q and q[0][0] <= time:
                heapq.heappush_max(maxHeap, q.popleft()[1])
            
        return time