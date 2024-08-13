class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        l,r = 0,0
        counter = [0,0,0]
        occurrences = 0
        while r < n:
            counter[ord(s[r]) - 97] += 1
            while counter[0] > 0 and counter[1] > 0 and counter[2]>0:
                occurrences += n -r
                counter[ord(s[l]) -97] -= 1
                l += 1
            r += 1
        return occurrences