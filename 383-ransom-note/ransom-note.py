class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = defaultdict(int)
        for letter in magazine:
            letters[letter] += 1
        for i in ransomNote:
            if i in letters:
                letters[i] -= 1
                if letters.get(i) == 0:
                    del letters[i]
            else:
                return False
        return True
    
        