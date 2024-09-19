class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(allowed)
        c = 0

        for word in words:
            for letter in word:
                if letter not in a:
                    break
            else:
                c += 1
        return c
