class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l = 0 
        r = 0
        while (r < len(word ))and word[r] != ch:
            r += 1
        word = list(word)
        if ch in word:
            while l < r:
                word[l],word[r] = word[r],word[l]
                l += 1
                r -= 1

        return "".join(word)