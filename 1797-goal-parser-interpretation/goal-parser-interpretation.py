class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        for i in range(len(command)):
            if command[i] =="G":
                ans += "G"
            elif command[i:i+2] == "()":
                ans += "o"
            elif command[i:i+2] == "(a":
                ans += "al"
        return ans