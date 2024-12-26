class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [-1,2,3,4]
        # left = [1,1,2,6]
        # right= [24,12,4,1]
        n = len(nums)
        left , right = [1]*n, [1]*n
        for i in range(1,n):
            left[i] = nums[i-1] * left[i-1]            
        for i in range(n-2,-1,-1):
            right[i] = nums[i+1] * right[i+1] 
        answer = [1] * n           
        for i in range(0,n):
            answer[i] = left[i] * right[i]
        return answer
