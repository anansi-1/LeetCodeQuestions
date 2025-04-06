class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # starting -> the smallest index equal to x
        starting = -1
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                starting = mid
                r = mid -1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        if starting == -1:
            return [-1,-1]
        ending = -1
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                ending = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return [starting,ending]