class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}

        def dfs(i, zeros, ones):
            if zeros > m or ones > n:
                return float('-inf')
            
            if i >= len(strs):
                return 0

            if (i, zeros, ones) in cache:
                return cache[(i, zeros, ones)]    
            
            z = strs[i].count("0")
            o = strs[i].count("1")

            take = 1 + dfs(i + 1, zeros + z, ones + o)
            skip = dfs(i + 1, zeros, ones)

            cache[(i, zeros, ones)] = max(take, skip)

            return cache[(i, zeros, ones)]

        return dfs(0, 0, 0)