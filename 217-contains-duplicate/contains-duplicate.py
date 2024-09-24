class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
        for i in count.values():
            if i > 1:
                return True
        return False