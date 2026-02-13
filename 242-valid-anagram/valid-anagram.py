class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two words are anagrams of eachother if they contain the same number and type of letter regardless of order

        if len(s) != len(t):
            return False
        
        occurrance_in_s = {}
        occurrance_in_t = {}

        for i in range(len(s)):
            occurrance_in_s[s[i]] = occurrance_in_s.get(s[i],0) + 1
            occurrance_in_t[t[i]] = occurrance_in_t.get(t[i],0) + 1


        return occurrance_in_s == occurrance_in_t