class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram_index = []
        p_count = [0]*26
        s_count = [0]*26
        for i in p:
            p_count[ord(i)-ord('a')] +=1
        for i in range(len(s)):
            s_count[ord(s[i])-ord('a')] += 1
            if i >= len(p):
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            if s_count == p_count:
                anagram_index.append(i - len(p) + 1)
        return anagram_index