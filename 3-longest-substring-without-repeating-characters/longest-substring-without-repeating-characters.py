class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = {}
        max_length = 0
        start = 0

        for i in range(len(s)):
            if s[i] in char and char[s[i]] >= start:
                start = char[s[i]] + 1

            char[s[i]] = i

            max_length = max(max_length, i - start + 1)

        return max_length
