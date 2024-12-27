class Solution:
    def removeOuterParentheses(self, S: str) -> str:       
        stack = []
        counter = 0

        for i in range(len(S)):
            if S[i] == "(":
                counter += 1
                if counter == 1:
                    pass
                else:
                    stack.append(S[i])
            if S[i] == ")":
                counter -= 1
                if counter == 0:
                    pass
                else:
                    stack.append(S[i])
        return "".join(stack)       