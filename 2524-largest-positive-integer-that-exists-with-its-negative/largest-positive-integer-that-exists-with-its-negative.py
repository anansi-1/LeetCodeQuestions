class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 0:
                if abs(nums[i]) in nums:
                    return abs(nums[i])

        return -1