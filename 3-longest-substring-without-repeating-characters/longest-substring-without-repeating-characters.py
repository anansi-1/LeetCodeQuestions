class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = {}
        window_start = 0
        current_length = 0
        longest = 0

        for i, letter in enumerate(s):
            if letter in sub and sub[letter] >= window_start:
                window_start = sub[letter] + 1
                current_length = i -sub[letter]
                sub[letter] = i
            else:
                sub[letter] = i
                current_length += 1
                if current_length > longest:
                    longest = current_length
        return longest