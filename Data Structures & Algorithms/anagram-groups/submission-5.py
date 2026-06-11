class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for item in strs:
            sortedItem = "".join(sorted(item))
            if sortedItem not in group:
                group[sortedItem] = [item]
            
            else:
                group[sortedItem].append(item)
        

        res = []
        for item in group.values():
            res.append(item)


        return res