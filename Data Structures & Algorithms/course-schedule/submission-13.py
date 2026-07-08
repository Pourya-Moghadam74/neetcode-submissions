class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visited = set()
        cycle = set()

        def dfs(i):
            if i in cycle:
                return False

            if i in visited:
                return True
            
            cycle.add(i)

            for nei in adj[i]:
                if dfs(nei) == False:
                    return False
            
            cycle.remove(i)
            visited.add(i)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        
        return True
        

            