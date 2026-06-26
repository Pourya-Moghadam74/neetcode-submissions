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
                node = heapq.heappop_max(maxHeap)
                if node - 1 > 0:
                    q.append((time + n, node - 1))

            if q:
                if q[0][0] <= time:
                    heapq.heappush_max(maxHeap, q[0][1])
                    q.popleft()
            
        return time