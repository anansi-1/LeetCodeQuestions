class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        max_avg = float('-inf')
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if i >= k -1:
                max_avg = max(max_avg, cur_sum/k)
                cur_sum -= nums[i - k + 1]
        return max_avg
