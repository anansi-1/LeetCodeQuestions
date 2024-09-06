class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqChar = {}
        for char in s:
            freqChar[char] = freqChar.get(char, 0) + 1
        
        for index in range(len(s)):
            char = s[index]

            if freqChar[char] == 1:
                return index
        
        return -1

