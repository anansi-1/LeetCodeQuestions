class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        for i in str(num):
            sum += int(i)
        if sum < 10:
            return sum
        else:
            return self.addDigits(sum)
        