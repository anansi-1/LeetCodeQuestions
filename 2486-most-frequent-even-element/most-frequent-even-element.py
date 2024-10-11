class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = []
        for number in nums:
            if number==0 or number%2==0:
                even.append(number)
        count = defaultdict(int) #{0:1 , 4:2, 1:1, 2:2}
        for i in even:
            count[i] += 1
        frequency = 0
        frequent = -1
        for num,occur in count.items():
            if occur > frequency or (occur==frequency and num < frequent):
                frequency = occur
                frequent = num
        return frequent



