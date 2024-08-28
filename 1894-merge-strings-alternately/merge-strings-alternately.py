class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = ""
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            mergedString = mergedString + word1[i]
            mergedString = mergedString + word2[j]
            i += 1
            j += 1
        while i < len(word1):
            mergedString = mergedString + word1[i]
            i += 1
        while j < len(word2):
            mergedString = mergedString + word2[j]
            j += 1
        return mergedString