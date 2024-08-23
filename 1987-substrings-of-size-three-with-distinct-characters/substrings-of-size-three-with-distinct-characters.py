class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        goodSubstrings = 0
        n = len(s) -2
        for i in range(n):
            if len(set(s[i:i+3])) == 3:
                goodSubstrings += 1
        return goodSubstrings