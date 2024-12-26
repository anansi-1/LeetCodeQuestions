class Solution:
    def pivotInteger(self, n: int) -> int:
        num = []
        for i in range(n+1):
            num.append(i)
        left = [0]*len(num)
        right = [0]*len(num)
        left[0] = num[0]
        right[-1] = num[-1]
        for i in range(1,len(num)):
            left[i] = left[i-1] + num[i]
        for i in range(len(num)-2,-1,-1):
            right[i] = right[i+1] + num[i]
        for i in range(len(num)):
            if left[i] == right[i]:
                return num[i]
        return -1
