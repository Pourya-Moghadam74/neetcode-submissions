class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        cycle = set()
        res = []

        def dfs(i):
            if i in cycle:
                return False
            
            if i in visited:
                return True
            
            cycle.add(i)
            for pre in preMap[i]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(i)
            visited.add(i)
            res.append(i)
            
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        
        return res