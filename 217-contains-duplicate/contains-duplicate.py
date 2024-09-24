class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number = {}
        for i in nums:
            if i in number:
                return True
            number[i] = number.get(i,0) + 1
        return False