class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = Counter(magazine)
        ransom_note_count = Counter(ransomNote)

        for letter in ransom_note_count:
            if ransom_note_count[letter] > magazine_count.get(letter,0):
                return False
        return True
    
        