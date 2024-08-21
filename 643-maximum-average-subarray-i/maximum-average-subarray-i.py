class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = float('-inf')
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            if i >= k-1:
                maxAvg = max(currentSum/k,maxAvg)
                currentSum -= nums[i-(k-1)]
        return maxAvg