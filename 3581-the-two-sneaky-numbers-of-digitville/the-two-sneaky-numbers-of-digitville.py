class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        ans = []
        for i in nums:
            if nums[i] > 1:
                ans.append(i)
        return ans