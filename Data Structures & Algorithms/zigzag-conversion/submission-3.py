class Solution:
    def convert(self, s: str, numRows: int) -> str:
        direction = -1
        res = ['' for _ in range(numRows)]
        curr = 0

        for i in range(len(s)):
            ch = s[i]

            if curr == 0 or curr == numRows - 1:
                direction *= -1
            
            res[curr] += ch
            curr += direction
        
        return "".join(res)