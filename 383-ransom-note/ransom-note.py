class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        magazine_count = Counter(magazine)
    
        ransom_note_count = Counter(ransomNote)

        for letter, count in ransom_note_count.items():
            if magazine_count[letter] < count:
                return False
        
        return True