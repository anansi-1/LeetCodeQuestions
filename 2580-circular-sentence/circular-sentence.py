class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()     # "leetcode" "eats" "soul"
        for i in range(len(s)-1): # 0          1        
            if s[i][-1] != s[i+1][0]:
                return False
        last_word = s[-1]
        first_word = s[0]
        if s[-1][-1] != s[0][0]:
            return False
        return True