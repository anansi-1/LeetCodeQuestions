class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)
        for i in ransomNote:
            if i in letters:
                letters[i] -= 1
                if letters.get(i) == 0:
                    del letters[i]
            else:
                return False
        return True
    
        