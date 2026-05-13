class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = {}
        res = []

        for item in strs:
            temp = "".join(sorted(item))
            if temp not in values:
                values[temp] = [item]
            else:
                values[temp] += [item]
        
        for item in values:
            res.append(values[item])

        return res
