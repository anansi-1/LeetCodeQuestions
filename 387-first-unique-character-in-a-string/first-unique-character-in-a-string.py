class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {} 
        for i in s:
            letters[i] = letters.get(i,0) + 1

        for i in letters:
            if letters[i] == 1:
                return (s.index(i))
                
        return -1

            
        