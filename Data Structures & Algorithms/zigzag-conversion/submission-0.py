class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res = [""] * numRows
        direction = -1
        i = 0

        for ch in s:
            res[i] += ch
            if i == 0 or i == numRows - 1:
                direction *= -1
            
            i += direction

        return "".join(res)