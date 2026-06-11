class Solution:
    def convert(self, s: str, numRows: int) -> str:
        direction = -1
        res = ["" for _ in range(numRows)]
        i = 0
        for c in s:
            if i == 0 or i == numRows - 1:
                direction *= -1
            
            res[i] += c
            i += direction
        
        return "".join(res)