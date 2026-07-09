class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visited = set()
        cycle = set()
        res = []

        def dfs(crs):
            if crs in visited:
                return True
            
            if crs in cycle:
                return False
            
            cycle.add(crs)

            for nei in adj[crs]:
                if dfs(nei) == False:
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
        
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        
        return res