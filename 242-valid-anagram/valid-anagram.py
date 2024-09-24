class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        for i in s:
            countS[i] = countS.get(i,0) + 1
        
        countT = {}
        for i in t:
            countT[i] = countT.get(i,0) + 1
        
        check = set(s+t)
        for letter in check:
            if countS.get(letter) != countT.get(letter):
                return False
        return True
                
        