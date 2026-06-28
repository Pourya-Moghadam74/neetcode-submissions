class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        cycle = set()

        def dfs(i):
            if i in cycle:
                return False
            
            cycle.add(i)

            for pre in preMap[i]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(i)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        
        return True