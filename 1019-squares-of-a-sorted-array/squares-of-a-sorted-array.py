class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) -1
        result = []
        while l <= r:
            if (nums[l]*nums[l]) >= (nums[r]*nums[r]):
                result.append(nums[l]*nums[l])
                l += 1
            else:
                result.append(nums[r]*nums[r])
                r -= 1
        result.reverse()
        return result