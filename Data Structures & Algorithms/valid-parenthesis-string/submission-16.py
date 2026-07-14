class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        ss = []

        for i, ch in enumerate(s):
            if ch == "(":
                st.append(i)
            
            elif ch == "*":
                ss.append(i)
            
            else:
                if st:
                    st.pop()
                
                elif ss:
                    ss.pop()
                
                else:
                    return False
        
        while st and ss:
            if st.pop() > ss.pop():
                return False
        
        return len(st) == 0

