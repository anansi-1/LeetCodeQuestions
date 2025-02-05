class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        count = 0
        for word in words:
            if not (Counter(word) - Counter(chars)):
                count += len(word)
        return count
      