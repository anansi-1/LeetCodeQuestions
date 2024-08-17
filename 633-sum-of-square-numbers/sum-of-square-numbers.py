class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        my_list = list(range(0,int( math.sqrt(c) ) + 1))
        l = 0
        r = len(my_list) - 1
        while l <= r:
            a = my_list[l]
            b = my_list[r]
            if  a*a+ b*b < c:
                l += 1
            elif a*a+ b*b > c:
                r -= 1
            elif a*a + b*b == c:
                return True
        return False