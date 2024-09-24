class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        for i in count.values():
            if i > 1:
                return True
        return False