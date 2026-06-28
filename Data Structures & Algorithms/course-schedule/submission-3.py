class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for p in prerequisites:
            preMap[p[0]].append(p[1])
        
        visited = set()

        def dfs(i):
            if len(preMap[i]) == 0:
                return True
            
            if i in visited:
                return False

            visited.add(i)

            for pre in preMap[i]:
                if not dfs(pre):
                    return False

            visited.remove(i)
            preMap[i] = []
            return True
        

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
