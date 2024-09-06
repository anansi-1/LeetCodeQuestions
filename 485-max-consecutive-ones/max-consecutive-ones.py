class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        max_consecutive = 0

        for i in nums:
            if i == 1:
                count += 1
            else:
                max_consecutive = max(count, max_consecutive)
                count = 0
        max_consecutive = max(count, max_consecutive)

        return max_consecutive