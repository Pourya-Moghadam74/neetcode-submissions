class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        q = deque()
        count = Counter(tasks)
        maxHeap = list(count.values())
        heapq.heapify_max(maxHeap)
        
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop_max(maxHeap)
                if cnt - 1 > 0:
                    q.append((time + n, cnt - 1))
                
            if q and q[0][0] <= time:
                time, cnt = q.popleft()
                heapq.heappush_max(maxHeap, cnt)
            
        return time