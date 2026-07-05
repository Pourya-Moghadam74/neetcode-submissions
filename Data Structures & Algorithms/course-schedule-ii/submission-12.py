class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        cycle = set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return True
            
            if crs in visited:
                return False
            
            cycle.add(crs)

            for nei in preMap[crs]:
                if dfs(nei) == True:
                    return True
                
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)

            return False
        
        for i in range(numCourses):
            if dfs(i) == True:
                return []
        
        return res

