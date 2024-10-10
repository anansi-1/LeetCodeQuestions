class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = []
        for n in nums:
            if n == 0 or n%2 == 0:
                even.append(n)
        dict = Counter(even)
        frequency = 0
        frequent = -1
        for n,c in dict.items():
            if c > frequency or (c==frequency and n<frequent):
                frequency = c
                frequent = n

        return frequent