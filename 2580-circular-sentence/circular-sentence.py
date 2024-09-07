class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split(" ")
        n = len(s)
        if n == 1:
            return sentence[0] == sentence[-1]

        valid = s[0][0] == s[-1][-1]
        if not valid:
            return valid

        return valid and all(
            map(lambda i: s[i][-1] == s[i+1][0], range(n-1))
        )