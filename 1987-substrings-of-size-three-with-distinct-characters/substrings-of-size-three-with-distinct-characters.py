class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return 0
        goodSubstring = 0
        a,b,c = s[0],s[1],s[2]

        for i in range(3,n):
            if a != b and b != c and a != c:
                goodSubstring += 1
            a,b,c = b,c,s[i]
        if a != b and b != c and a != c:
            goodSubstring += 1
        return goodSubstring 