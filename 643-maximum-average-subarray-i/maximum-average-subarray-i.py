class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = 0
        max_sum = float('-inf')

        for i in range(len(nums)): 
            summ += nums[i]
            if i >= k-1:
                cur_avg = summ/k
                summ -= nums[(i-k)+1]
                max_sum = max(cur_avg,max_sum)
        return max_sum