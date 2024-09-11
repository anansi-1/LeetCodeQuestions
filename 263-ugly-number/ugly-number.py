class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        uglies = [2, 3, 5]

        for u in uglies:
             while n % u == 0:
                n = n // u
        return n == 1