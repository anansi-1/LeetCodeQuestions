class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = ""
        for i in range(len(spaces)):
            if i == 0:
                output += s[:spaces[i]] + " "
            else:
                output+=s[spaces[i-1]:spaces[i]]+" "
        output+=s[spaces[len(spaces)-1]:]
        return output
