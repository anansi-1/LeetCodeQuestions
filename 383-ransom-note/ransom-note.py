class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for letter in magazine:
            letters[letter] = letters.get(letter, 0) + 1
        for i in ransomNote:
            if i in letters:
                letters[i] = letters.get(i) - 1
                if letters.get(i) == 0:
                    del letters[i]
            else:
                return False
        return True
    
        