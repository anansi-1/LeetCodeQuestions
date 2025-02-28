class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = []
        running_sum = 0
        for i in range(0,len(nums)):
            running_sum += nums[i]
            prefix_sum.append(running_sum)
        min_sum = 0
        max_sum = float('-inf')
        for i in range(len(prefix_sum)):
            max_sum = max(max_sum,prefix_sum[i]-min_sum)
            min_sum = min(min_sum,prefix_sum[i])
        
        return max_sum