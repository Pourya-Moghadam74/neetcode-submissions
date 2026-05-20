class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        word = strs[0]
        i = 0
        while i < len(word):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or word[i] != strs[j][i]:
                    return res
            
            res += word[i]
            i += 1
        
        return res
