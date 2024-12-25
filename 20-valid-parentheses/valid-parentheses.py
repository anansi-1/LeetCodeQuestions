class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {"(":")", "[":"]","{":"}"}
        stack = []
        for i in s:
            if i in bracket_pairs:
                stack.append(i)
                continue
            if len(stack)!=0 and bracket_pairs[stack[-1]] == i:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
                
            
            