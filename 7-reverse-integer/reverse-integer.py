class Solution:
    def reverse(self, x: int) -> int:
        minm = -2147483648
        maxm = 2147483647
        res = 0
        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)

            if(res > maxm // 10 or (res == maxm //10 and digit >= maxm %10)):
                return 0
            if(res < minm // 10 or (res == minm //10 and digit <= minm %10)):
                return 0
            res = (res*10) + digit
        return res