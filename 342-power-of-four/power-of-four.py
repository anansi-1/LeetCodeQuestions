class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        while n >= 4:
            if n == 4:
                return True
            else:
                n = n/4
        return False