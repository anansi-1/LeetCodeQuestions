class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for i in range(len(s)):
            if s[i] == "*":
                stk.pop()
                continue
            stk.append(s[i])  
        s = "".join(stk)
        return s
            