class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        i = 0
      
        n = len(nums)
        while i < n-1:
            if (nums[i]%2==nums[i+1]%2):
                return False
            i += 1
        return True
           