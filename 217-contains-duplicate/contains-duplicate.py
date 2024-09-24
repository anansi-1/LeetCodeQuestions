class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # 1,1,2,3
        for i in range(len(nums)-1): # 0 1 2 3
            if nums[i] != nums[i+1]:
                continue
            else:
                return True

