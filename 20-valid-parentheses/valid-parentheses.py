class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        close = {")":"(","]":"[","}":"{"}
        arr = []
        for i in s:
            if i in close and len(arr) != 0:
                if close[i] == arr[-1]:
                    arr.pop()
                else:
                    return False  
            else:
                arr.append(i)
        if len(arr) != 0:
            return False
        return True