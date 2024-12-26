class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        right = [15,11,3,0]
        left , right = [0] * len(nums), [0]* len(nums)
        answer = [0] * len(nums)
        for i in range(1,len(nums)):
            left[i] = left[i-1] + nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1] + nums[i+1]
        answer = [0]*len(nums)
        for i in range(0,len(nums)):
            answer[i] = abs(left[i]-right[i])
        return answer