class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            total = 0
            for ch in str(n):
                total += int(ch) ** 2
            
            if total == 1:
                return True
            
            if total in seen:
                return False
            else:
                seen.add(total)
            
            n = total