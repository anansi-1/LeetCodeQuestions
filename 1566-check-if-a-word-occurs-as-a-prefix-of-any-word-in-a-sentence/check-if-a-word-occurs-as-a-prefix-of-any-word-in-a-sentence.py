class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        for i in range(len(sentence)):
            if searchWord in sentence[i][:len(searchWord)]:
                return i+1
        return -1
