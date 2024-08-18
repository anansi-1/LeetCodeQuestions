class Solution:
    def addDigits(self, num: int) -> int:
        total_sum = 0
        for i in str(num):
            total_sum += int(i)
        if total_sum < 10:
            return total_sum
        else:
            return self.addDigits(total_sum)