class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in s:
            found_index = t[j:].find(i)
            if found_index == -1:
                return False
            j += found_index + 1
            
        return True