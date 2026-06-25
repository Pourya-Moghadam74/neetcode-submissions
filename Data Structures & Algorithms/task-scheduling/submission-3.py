class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        q = deque()
        count = Counter(tasks)
        maxHeap = [cnt for cnt in count.values()]
        heapq.heapify_max(maxHeap)

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop_max(maxHeap)
                if cnt > 1:
                    q.append((cnt - 1, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q[0][0])
                q.popleft()
            
        
        return time