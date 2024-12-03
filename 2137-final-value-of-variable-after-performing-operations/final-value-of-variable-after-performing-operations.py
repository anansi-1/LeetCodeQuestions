class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            j = i.replace("X","")
            if j == "--":
                x -= 1
            elif j =="++":
                x += 1
        return x