class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        maxHeap = list(count.values())
        heapq.heapify_max(maxHeap)
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                t = heapq.heappop_max(maxHeap)
                if t - 1 > 0:
                    q.append((t - 1, time + n))
            
            if q and q[0][1] <= time:
                t = q.popleft()
                heapq.heappush_max(maxHeap, (t[0]))
            
        return time
