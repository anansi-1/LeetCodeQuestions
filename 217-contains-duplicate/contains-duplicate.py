class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number = {}
        for i in nums:
            if i not in number:
                number[i] = number.get(i,0) + 1
            else:
                return True
        return False