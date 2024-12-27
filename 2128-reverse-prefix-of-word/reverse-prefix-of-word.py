class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        stack = []
        letters = list(word)   #[a , b, c , d, e,f , d]
        for i in range(len(word)): #7
            if word[i] == ch:
                stack.append(word[i])
                break
            stack.append(word[i]) # [a,b,c,d] 

        i = 0
        while len(stack) > 0:
            letters[i] = stack.pop()
            i += 1
        word = "".join(letters)
        return word