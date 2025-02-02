class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums= []
        for letter in s:
            nums.append(ord(letter)-96)
        #"12552031545" 
        nums = "".join(map(str,nums))
        for i in range(k):
            res = 0
            for num in nums:
                res += int(num)
            nums = str(res)
        return res


