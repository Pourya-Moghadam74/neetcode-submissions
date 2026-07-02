class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        cycle = set()

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
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True