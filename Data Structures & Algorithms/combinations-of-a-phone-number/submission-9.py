class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, path):
            if len(path) == len(digits):
                res.append(path)
                return
            
            for c in digitToChar[digits[i]]:
                dfs(i + 1, path + c)
            
        if digits:
            dfs(0, "")

        return res
