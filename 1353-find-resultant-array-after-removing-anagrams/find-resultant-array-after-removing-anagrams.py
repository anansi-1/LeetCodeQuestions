class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        for word in words:
            stack.append(word)

            if len(stack) >= 2 and sorted(stack[-1])== sorted(stack[-2]):
                stack.pop()
        return  stack