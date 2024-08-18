class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        n = len(digits)
        for i in digits:
            num = num * 10 + i
        num += 1
        num = list(str(num))
        ans = []
        for i in num:
            ans.append(int(i))
        return ans