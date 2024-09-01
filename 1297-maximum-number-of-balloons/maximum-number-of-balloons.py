class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < len("balloon"):
            return 0

        count_letters = {}

        for i in text:
            count_letters[i] = count_letters.get(i,0) + 1
        
        flag = True
        count = 0

        while flag:
            for i in "balloon":
                if i in count_letters:
                    count_letters[i] -= 1
                    if count_letters[i] == 0:
                        del count_letters[i]
                else:
                    flag = False
                    break
            if flag:
                count += 1
        return count
